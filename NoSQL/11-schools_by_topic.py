#!/usr/bin/env python3
"""
Get schools by topic
"""
from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
	"""
	lists schools by topic
	"""
	result = mongo_collection.find({"topics": topic})
	return result