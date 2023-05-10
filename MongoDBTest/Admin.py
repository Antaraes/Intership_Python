import pymongo

connection = pymongo.MongoClient('localhost',27017)
database = connection['crud_test']
collection = database['admin']
admin1 = {"name":"ajm","email":"ajm@gmail.com","password":"pass"}

def insert_Admin():
    print("Welcome add admin section")
    name = input("Enter name:")
    email = input("Enter email:")
    password = input("Enter password:")
    dataformat = {"name":name,"email":email,"password":password}
    try:
        obj = collection.insert_one(dataformat)
        print("Data are successfully Inserted")
    except Exception as err:
        print(err)

def show_Admins():

    for i in collection.find({}, {"_id": 0}):
        print(i)