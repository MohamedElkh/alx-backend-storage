#!/usr/bin/env python3
"""script provides stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


def func_log(mongo_collection):
    """func provides stats about Nginx logs stored in MongoDB"""
    total_x = mongo_collection.count_documents({})
    print("{} logs".format(total_x))
    print("Methods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for meth in methods:
        docs = mongo_collection.count_documents({"method": meth})
        print("\tmethod {}: {}".format(meth, docs))

    st = mongo_collection.count_documents({"method": "GET",
                                           "path": "/status"})
    print("{} status check".format(st))


if __name__ == "__main__":
    with MongoClient() as client:
        db = client.logs

        collect = db.nginx
        log_stats(collect)
