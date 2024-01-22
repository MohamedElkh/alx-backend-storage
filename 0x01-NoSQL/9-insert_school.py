#!/usr/bin/env python3
"""this doc have func to insert docs"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """func to insert to school"""
    return mongo_collection.insert_one(kwargs).inserted_id
