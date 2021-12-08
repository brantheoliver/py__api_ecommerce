from flask_marshmallow import Marshmallow

from .models import Order, Item

ma = Marshmallow()


def config_ma(app):
    ma.init_app(app)


class OrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Order
        load_instance = True


class ItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Item
        load_instance = True
