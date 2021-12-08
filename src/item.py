from flask import Blueprint, request, current_app, jsonify

from .models import Item
from .schemas import ItemSchema

item = Blueprint("item", __name__, url_prefix="/item")


@item.route("/edit/<product_id>", methods=["PUT"])
def edit_price(product_id):
    new_price = request.json["new_price"]
