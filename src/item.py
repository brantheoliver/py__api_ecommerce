from flask import Blueprint, request, current_app, jsonify

from .models import Item
from .schemas import ItemSchema

item = Blueprint("item", __name__, url_prefix="/item")


@item.route("/edit/<product_id>", methods=["PUT"])
def edit_price(product_id):
    data = request.get_json()
    item = Item.query.get(product_id)

    if data.get("new_price"):
        item.unit_price = data["new_price"]
    else:
        return jsonify({"message": "Bad Request"}), 400

    if not item:
        return jsonify({"message": "Item not found."}), 404

    current_app.db.session.add(item)
    current_app.db.session.commit()

    item_schema = ItemSchema()
    result = item_schema.dump(item)

    return jsonify(result)
