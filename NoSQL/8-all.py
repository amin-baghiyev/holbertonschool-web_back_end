#!/usr/bin/env python3
"""
List all collection
"""


def list_all(mongo_collection):
	"""
	list collection
	"""
	return mongo_collection.find()