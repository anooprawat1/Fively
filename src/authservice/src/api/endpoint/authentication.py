from fastapi import APIRouter
from src.schema.user import LoginSchema
from keycloak import KeycloakOpenID, KeycloakAdmin

router = APIRouter()

keyclock_openid = KeycloakOpenID(
    server_url="http://keycloak:8080/auth/",
    client_id="account",
    realm_name="Fively",
    client_secret_key="RIMM2sNguBMoIWFNTHzSo9wllbB9IL6q")


@router.post("/register")
def register_user():
    return {"Hello": "World"}


@router.post("/token")
def get_access(login_schema: LoginSchema):
    keycloak_openid = KeycloakOpenID(server_url="http://keycloak:8080/auth/",
                                     client_id="account",
                                     realm_name="Fively",
                                     client_secret_key="RIMM2sNguBMoIWFNTHzSo9wllbB9IL6q")
    token = keycloak_openid.token(
        str(login_schema.email_id), login_schema.password)
    if token:
        userinfo = keycloak_openid.userinfo(token['access_token'])
        print("USERINFO--------------", userinfo)


@router.post("/forget_password")
def forget_password():
    pass
