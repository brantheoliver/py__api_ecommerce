from flask import Flask, jsonify
from flask_migrate import Migrate

import os
from .order import order
from .item import item
from .models import config_db
from .schemas import config_ma


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = os.environ.get(
        "SQLALCHEMY_TRACK_MODIFICATIONS"
    )

    config_db(app)
    config_ma(app)
    Migrate(app, app.db)

    app.register_blueprint(order)
    app.register_blueprint(item)

    @app.errorhandler(400)
    def handle_400_error(e):
        return jsonify({"error": "ERROR 400: Bad Request."}), 400

    @app.errorhandler(404)
    def handle_404_error(e):
        return jsonify({"error": "ERROR 404: Not found."}), 404

    @app.errorhandler(500)
    def handle_500_error(e):
        return jsonify({"error": "ERROR 500: Internal Server Error."}), 500

    return app
