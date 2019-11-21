from pymongo import MongoClient

MONGO_CONNECTION_STRING = ''

## Test connect to mongodb
##TODO: secure connect to mongo db

def test():
    client = MongoClient(MONGO_CONNECTION_STRING.format())
    db = client.test

def get_client():
    return = MongoClient(MONGO_CONNECTION_STRING)

def get_db(client, db_name):
    return client[db_name]

def get_collection(db, col_name):
    return db[col_name]


client = get_client()
members_db = get_db(client, 'fftball')
collection = get_collection(members_db, 'members')
test()