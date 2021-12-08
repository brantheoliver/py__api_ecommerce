from flask import Blueprint, request, current_app

from .models import Item
from .schemas import ItemSchema

item = Blueprint("item", __name__, url_prefix="/item")


@item.route("/edit/<new_price>")
def edit_price(new_price):
    pass
