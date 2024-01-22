#!/usr/bin/env python3
"""this doc have func to change school topic"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """func to update many rows"""
    return mongo_collection.update_many({"name": name},
                                        {"$set": {"topics": topics}})
