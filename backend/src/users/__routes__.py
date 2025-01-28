from src.users.models import AddUser, DeleteUser, GetUser, GetUsers, UpdateUser
from . import users_api

users_api.add_resource(GetUsers, "/users")
users_api.add_resource(GetUser, "/user/<id>")
users_api.add_resource(DeleteUser, "/delete/user/<id>")
users_api.add_resource(UpdateUser, "/update/user/<id>")
users_api.add_resource(AddUser, "/user")

