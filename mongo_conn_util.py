from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")

db = client["bank"]


account_collection = db["accounts"]


def get_account_collection():
    return account_collection


def close_connection():
    client.close()
