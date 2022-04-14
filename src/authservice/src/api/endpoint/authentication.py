import os
from dotenv import load_dotenv, find_dotenv
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from src.schema.user import ForgetSchema
from src.schema.user import CreateUserSchema
from src.schema.user import LoginSchema
from keycloak import KeycloakOpenID, KeycloakAdmin

load_dotenv(find_dotenv())
KEYCLOAK_PUBLIC_KEY = "-----BEGIN PUBLIC KEY-----\n" + \
    os.environ.get("keycloak_public_key", "") + "\n-----END PUBLIC KEY-----"
KEYCLOAK_SERVER_URL = os.environ.get("keycloak_server_url")
KEYCLOAK_CLIENT_ID = os.environ.get("keycloak_client_id")
KEYCLOAK_REALM_NAME = os.environ.get("keycloak_realm_name")
KEYCLOAK_CLIENT_SECRET_KEY = os.environ.get("keycloak_client_secret_key")
KEYCLOAK_ADMIN_USERNAME = os.environ.get("keycloak_admin_user")
KEYCLOAK_ADMIN_PASSWORD = os.environ.get("keycloak_admin_password")

router = APIRouter()
keycloak_openid = KeycloakOpenID(
    server_url=KEYCLOAK_SERVER_URL,
    client_id=KEYCLOAK_CLIENT_ID,
    realm_name=KEYCLOAK_REALM_NAME)

keycloak_admin = KeycloakAdmin(server_url=KEYCLOAK_SERVER_URL,
                               username='admin@admin.com',
                               password='admin',
                               realm_name=KEYCLOAK_REALM_NAME,
                               verify=False)


@router.post("/register")
def register_user(user_create: CreateUserSchema):
    try:
        new_user = keycloak_admin.create_user({"email": user_create.email_id,
                                               "username": user_create.email_id,
                                               "enabled": True,
                                               "firstName": user_create.first_name,
                                               "lastName": user_create.last_name,
                                               "credentials": [{"value": user_create.password, "type": "password", }]},
                                              exist_ok=False)
        if new_user is not None:
            raise HTTPException(
                status_code=400, detail="User already created")

        return JSONResponse(
            status_code=200,
            content={
                "message": f"User successfully created"},
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail="User already exist")


@router.post("/token")
def get_access(login_schema: LoginSchema):
    try:
        token = keycloak_openid.token(
            str(login_schema.email_id), login_schema.password)
        if token:
            return JSONResponse(
                status_code=200,
                content={
                    "access_token": f"{token['access_token']}",
                    "refresh_token": f"{token['refresh_token']}",
                    "expires_in": f"{token['expires_in']}",
                    "refresh_expires_in": f"{token['refresh_expires_in']}",
                    "token_type": f"{token['token_type']}"},
            )
        raise HTTPException(status_code=403, detail={
            "message": "Wrong email and password"})

    except Exception as e:
        raise HTTPException(status_code=403, detail={
            "message": "Wrong email and password"})


@router.post("/forget_password")
def forget_password(forget_schema: ForgetSchema):
    try:
        user_id = keycloak_admin.get_user_id(username=forget_schema.email_id)
        keycloak_admin.set_user_password(
            user_id=user_id, password=forget_schema.password, temporary=False)
    except Exception as e:
        raise HTTPException(status_code=403, detail={
            "message": "Not working right now"})
