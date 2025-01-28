from flask import request
from flask_restful import Resource

from config.utilis import uniqueId
from config.db import mongo

mdb = mongo.db
if mdb is not None:
    db = mdb["users"]
else:
    raise RuntimeError(
        "MongoDB connection failed. Check your URI and database configuration."
    )


class GetUsers(Resource):
    def get(self):
        users = []
        for user in db.find():
            users.append(
                {
                    "_id": str(user["_id"]),
                    "name": user["name"],
                    "email": user["email"],
                    "password": user["password"],
                }
            )
        return users


class GetUser(Resource):
    def get(self, id):
        user = db.find_one({"_id": id})
        if user is not None:
            user["_id"] = str(user["_id"])
        else:
            user = {}
        return {"user": user}


class DeleteUser(Resource):
    def get(self, id):
        print(f"id: {id}")
        if id is not None:
            db.delete_one({"_id": id})
        else:
            id = None
        return {
            "status": 1,
            "cls": "success",
            "message": "User deleted.",
            "payload": {"id": id},
        }


class AddUser(Resource):
    def post(self):
        inputData = request.get_json(silent=True)

        user = db.insert_one(
            {
                "_id": uniqueId(isNum=True, prefix="U"),
                "name": inputData["name"],
                "email": inputData["email"],
                "password": inputData["password"],
            }
        )
        inserted_id = user.inserted_id
        return {
            "status": 1,
            "cls": "success",
            "message": "User created successfully.",
            "payload": {"_id": str(inserted_id)},
        }


class UpdateUser(Resource):
    def post(self, id):
        inputData = request.get_json(silent=True)

        db.update_one(
            {"_id": id},
            {
                "$set": {
                    "name": inputData["name"],
                    "email": inputData["email"],
                    "password": inputData["password"],
                }
            },
        )
        return {
            "status": 1,
            "cls": "success",
            "message": "User Updated.",
            "payload": {"_id": id},
        }
