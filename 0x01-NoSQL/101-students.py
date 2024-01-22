#!/usr/bin/env python3
"""doc contain func to students"""


def top_students(mongo_collection):
    """func to score students"""
    return mongo_collection.aggregate([
        {
            "$project":
            {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {
            "$sort":
            {
                "averageScore": -1
            }
        }
    ])
