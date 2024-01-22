#!/usr/bin/env python3
"""script to provides stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_logs = client.logs.nginx

    docs_n = nginx_logs.count_documents({})
    get_n = nginx_logs.count_documents({'method': 'GET'})

    post_n = nginx_logs.count_documents({'method': 'POST'})
    put_n = nginx_logs.count_documents({'method': 'PUT'})
    patch_n = nginx_logs.count_documents({'method': 'PATCH'})

    delete_n = nginx_logs.count_documents({'method': 'DELETE'})
    get_status = nginx_logs.count_documents({'method': 'GET', 'path': '/status'})

    print("{} logs".format(docs_n))
    print("Methods:")

    print("\tmethod GET: {}".format(get_n))
    print("\tmethod POST: {}".format(post_n))
    print("\tmethod PUT: {}".format(put_n))

    print("\tmethod PATCH: {}".format(patch_n))
    print("\tmethod DELETE: {}".format(delete_n))

    print("{} status check".format(get_status))
