
import string
from random import choice
from .db import mongo


db = mongo.db


def numGenerator(size=6, chars=string.digits):
    return "".join(choice(chars) for x in range(size))

def alphaNumGenerator(size=4, chars="ABCDEFGHJKLMNPQRSTUVWYZ123456789"):
    return "".join(choice(chars) for x in range(size))

def uniqueId(digit=4, isNum=False, ref={}, prefix=None, suffix=None):
    _id = numGenerator(digit) if isNum else alphaNumGenerator(digit)

    if prefix is not None:
        _id = f"{prefix}X{_id}"

    if suffix is not None:
        _id = f"{_id}X{suffix}"

    mUniqueIds = db.uuid
    data = mUniqueIds.find_one({"_id": _id})

    if data and "_id" in data:
        return uniqueId(digit, isNum, ref, prefix, suffix)
    else:
        if ref and "_id" in ref:
            ref.pop("_id")
        mUniqueIds.insert_one({"_id": _id, **ref})
        return _id