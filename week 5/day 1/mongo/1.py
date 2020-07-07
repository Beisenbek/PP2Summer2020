import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["my-customers"]

mydict = { "name": "Arman3", "address": "Tole bi 59" }

x = mycol.insert_one(mydict)

print(x.inserted_id)