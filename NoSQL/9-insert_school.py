#!/usr/bin/env python3
"""
Insertion into collection
"""
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
	"""
	Insert a new datum into the specified MongoDB collection
	"""
	result = mongo_collection.insert_one(kwargs)
	return result.inserted_id