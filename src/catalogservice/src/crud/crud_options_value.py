import uuid
from src.models.options_value import OptionValue
from src.database.database import get_db
from sqlalchemy.orm import Session


class CrudOptionsValue:

    def session(self) -> Session:
        return get_db()

    def add_option_option(self, name: str, product_id, option_id):
        if not self.is_option_value_exist(name, product_id, option_id):
            option_value = OptionValue(
                name=name, product_id=product_id, option_id=option_id)
            self.session().add(option_value)
            self.session().commit()
        return self.get_option_value_id_for_option(name, product_id, option_id)

    def is_option_value_exist(self, name: str, product_id: uuid.UUID, option_id: uuid.UUID) -> bool:
        return self.session().query(OptionValue).filter(OptionValue.name == name, OptionValue.option_id == option_id, OptionValue.product_id == product_id).first() is not None

    def get_option_value_id_for_option(self, name: str, product_id: uuid.UUID, option_id: uuid.UUID):
        option_value = self.session().query(OptionValue).filter(OptionValue.name == name,
                                                                OptionValue.option_id == option_id, OptionValue.product_id == product_id).first()
        if option_value is not None:
            return option_value.id
        else:
            return None


crud_options_value = CrudOptionsValue()
