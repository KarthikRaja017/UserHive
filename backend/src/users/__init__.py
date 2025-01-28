from flask import Blueprint
from flask_restful import Api

users_bp = Blueprint('users', __name__,url_prefix='/server/api')
users_api = Api(users_bp)

from . import __routes__