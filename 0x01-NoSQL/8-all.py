#!/usr/bin/env python3
"""this docs have func to list all docs"""
import pymongo


def list_all(mongo_collection):
    """func to list all collection"""
    if not mongo_collection:
        return []

    return list(mongo_collection.find())
