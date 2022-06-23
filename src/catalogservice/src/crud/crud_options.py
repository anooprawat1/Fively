import uuid
from src.models.options import Options
from src.database.database import get_db
from sqlalchemy.orm import Session


class CrudOptions:

    def session(self) -> Session:
        return get_db()

    def add_option(self, name: str, product_id):
        if not self.is_option_exist(name, product_id):
            option = Options(name=name, product_id=product_id)
            self.session().add(option)
            self.session().commit()
        return self.get_option_id_for_option(name, product_id)

    def is_option_exist(self, name: str, product_id: uuid.UUID) -> bool:
        return self.session().query(Options).filter(Options.name == name, Options.product_id == product_id).first() is not None

    def get_option_id_for_option(self, name: str, product_id: uuid.UUID):
        option = self.session().query(Options).filter(
            Options.name == name, Options.product_id == product_id).first()
        if option is not None:
            return option.id
        else:
            return None


crud_options = CrudOptions()
