#!/usr/bin/env python3
"""this doc have func to find by topic"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """func to find by topic"""
    return mongo_collection.find({"topics": topic})
