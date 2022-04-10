from pymongo import MongoClient
from buildDataTree.buildTree import *
from getResult import getResult

while True:
    print("=============Connection================")
    host = input("The MongoDB host is [Default:'localhost']:\n")
    if not(host):
        host = "localhost"

    
    while True:
        port = input("The MongoDB port is [Default:27017]:\n")
        if port:
            try:
                port = int(port)
                break
            except:
                print("Input for port is invalid.\n")
        else:
            port = 27017
            break

    try:    
        client = MongoClient(host,port)
        print("The connection to MongoDB is successful.\n")
        break
    except:
        print("The connection to MongoDB is failed.\n")

while True:
    print("\n=============Database================")
    db_name = input("The database name is :\n")
    
    if db_name:
        db = client[db_name]
    else:
        print("Input for database name is invalid.\n")

    cl_name = input("The collection name is :\n")
    
    if not(cl_name):
        print("Input for collection name is invalid.\n")

    try:
        db_data = list(db[cl_name].find({}))
        print("The data is imported.")
    except:
        print("Cannot get data from the database collection.\n")



    data_tmp = db_data[0]
    data = dict()
    for key in data_tmp:
        if key == "_id":
            continue
        else:
            data[key] = data_tmp[key]

    try:
        root = buildTree(data)
        break
    except:
        print("The data is invalid.")

                
while True:
    print("\n=============Xpath================")

    query = input("Your Xpath query is:\n")

    if query:
        try:
            print("\n",getResult(data,query),"\n")
        except:
            print("\nInput is valid.")
    else:
        query = input("Your Xpath query is:\n")

                                
