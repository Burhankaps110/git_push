import pymongo


client = pymongo.MongoClient("mongodb://Burhankapadia:786110252Bu$@burhanuddin-shard-00-00.khuvc.mongodb.net:27017,burhanuddin-shard-00-01.khuvc.mongodb.net:27017,burhanuddin-shard-00-02.khuvc.mongodb.net:27017/?ssl=true&replicaSet=atlas-r11xdq-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test

d = {
    "name" : "Burhanuddin",
    "email_id" : "burhankaps110@gmail.com",
    "surname" : "Kapadia"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)

