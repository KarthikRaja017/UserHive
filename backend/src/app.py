import os
from flask import Flask, send_from_directory
from flask_cors import CORS
from src.config.db import mongo


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    CORS(app, resources={r"/*": {"origins": "*"}})
    mongo.init_app(app)
    # frontend_folder = os.path.abspath(os.path.join(os.getcwd(), "..", "frontend"))
    # dist_folder = os.path.join(frontend_folder, "dist")
    
    # @app.route("/", defaults={"filename": ""})
    # @app.route("/<path:filename>")
    # def index(filename):
    #     if filename and os.path.exists(os.path.join(dist_folder, filename)):
    #         return send_from_directory(dist_folder, filename)
    #     else:
    #         return send_from_directory(dist_folder, "index.html")
        
    from src.users import users_bp
    app.register_blueprint(users_bp)
    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
