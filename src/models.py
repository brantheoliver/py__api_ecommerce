from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref

db = SQLAlchemy()


def config_db(app):
    db.init_app(app)
    app.db = db


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(100))

    items = db.relationship("Item", backref="order")

    def __init__(self, client_id, status) -> None:
        self.client_id = client_id
        self.status = status


class Item(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.Text, nullable=False)
    unit_price = db.Column(db.Float, nullable=False)

    order_id = db.Column(db.Integer, db.ForeignKey("order.id"), nullable=False)

    def __init__(self, descricao, unit_price, order_id) -> None:
        self.descricao = descricao
        self.unit_price = unit_price
        self.order_id = order_id

    def __repr__(self):
        return {
            "product_id": self.product_id,
            "descricao": self.descricao,
            "unit_price": self.unit_price,
            "order_id": self.order_id,
        }
