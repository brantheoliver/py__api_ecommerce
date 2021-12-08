from flask import Blueprint, request, current_app, jsonify

from .models import Order, Item
from .schemas import OrderSchema, ItemSchema

order = Blueprint("order", __name__, url_prefix="/order")

# Done!
@order.route("/create", methods=["POST"])
def create_order():
    client_id = request.json["client_id"]
    status = request.json["status"]

    new_order = Order(client_id, status)
    order_schema = OrderSchema()

    current_app.db.session.add(new_order)
    current_app.db.session.commit()

    return order_schema.jsonify(new_order), 201


# Done!
@order.route("/add/<order_id>", methods=["POST"])
def add_item(order_id):
    descricao = request.json["descricao"]
    unit_price = request.json["unit_price"]

    new_item = Item(descricao, unit_price, order_id)
    item_schema = ItemSchema()

    current_app.db.session.add(new_item)
    current_app.db.session.commit()

    return item_schema.jsonify(new_item), 201


# Done!
@order.route("/remove/<order_id>", methods=["DELETE"])
def remove_item(order_id):
    item = Item.query.filter_by(order_id=order_id).first()
    item_schema = ItemSchema()

    current_app.db.session.delete(item)
    current_app.db.session.commit()

    return item_schema.jsonify(item)


# Done!
@order.route("/delete/<order_id>", methods=["DELETE"])
def cancel_order(order_id):
    order = Order.query.get(order_id)
    order_schema = OrderSchema()

    current_app.db.session.delete(order)
    current_app.db.session.commit()
    return order_schema.jsonify(order)


# Done!
@order.route("/items/<order_id>", methods=["GET"])
def get_order_items(order_id):
    items = Item.query.filter_by(order_id=order_id).all()

    item_schema = ItemSchema(many=True)
    result = item_schema.dump(items)

    return jsonify(result)
