from flask import Flask, request, jsonify
from flask_cors import CORS
from config.db import mongo


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    CORS(app, resources={r"/*": {"origins": "*"}})
    mongo.init_app(app)
    from users import users_bp

    app.register_blueprint(users_bp)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
