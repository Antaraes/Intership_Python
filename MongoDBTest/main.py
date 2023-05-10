import pymongo
from Admin import insert_Admin,show_Admins
connection = pymongo.MongoClient('localhost',27017)
database = connection['crud_test']
collection = database['students']
collection_admin = database['admin']
dataList = []

def main():
    try:
        print("To Login press 1\nTo register press 2\nTo exit from app press 3")
        userinput = int(input("enter your choice:"))
        if userinput == 1:
            login()
        elif userinput == 2:
            register()
        elif userinput == 3:
            exit(1)
        else:
            print("Invalid Option")
            main()
    except ValueError:
        print("Incorrect Input Try again")
        main()

def admin():
    try:
        print("Welcome Admin")
        print("To Add Student Data press 1\nTo ShowData press 2\nTo add another admin press 3 \n To show Admins Data press 4 \nTo quit from admin press 5 \nTo delete Account press 6 \nsection To Exit press 7")
        userinput = int(input("Enter Your answer:"))
        if userinput == 1:
            insert_Data(None)
        elif userinput == 2:
            showData()
        elif userinput == 3:
            insert_Admin()
        elif userinput == 4:
            show_Admins()
        elif userinput == 5:
            main()
        elif userinput == 6:
            delete_data()
        elif userinput == 7:
            insert_DB(dataList)
            exit(1)
        else:
            print("Invalid Option")
            admin()
    except ValueError:
        print("Incorrect Input Try again")
def login():
    print("Login Sector")

    try:
        email = input("Enter your email to login:")
        query = {"email":email}
        data = collection.find(query,{"_id":0})
        data2 = collection_admin.find(query,{"_id":0})
        if data2:
            for i in data2:
                password = input("Enter your password to login:")
                if i['password'] == password:
                    admin()
        if data:
            for i in data:
                if i['password'] == password:
                    print(i)
        else:
            reLogin()
    except Exception as err:
        print(err)

def reLogin():
    print("incorrect email or password")
    try:
        userinput = int(input("To exit to Home page press 1 or continue to login press 2:"))
        if userinput == 1:
            main()
        elif userinput == 2:
            login()
        else:
            print("Invalid Error")
            reLogin()
    except ValueError:
        print("Incorrect input just input number!")

def register():
    user_email = input("Enter your email:")
    email_Check = Email_exist(user_email)
    if email_Check != None:
        print("Email already exit.")
        register()
    else:
        insert_Data(user_email)

def Email_exist(email):
    query = {"email":email}
    data = collection.find(query)
    for i in data:
        if i['email'] == email:
            return data
def showData():
    insert_DB(dataList)
    print("To show All data press 1 \nTo search with name press 2\nTo show ascending data press 3\nTo descending data press 4")
    user_input = int(input("Enter your answer:"))
    if user_input == 1:
        for i in collection.find({},{"_id":0}):
            print(i)
    elif user_input == 2:
        user_search = input("Enter your search name:")
        query = {"name":{"$regex":f"^{user_search}"}}
        for i in collection.find(query,{"_id":0}):
            print(i)
    elif user_input == 3:
        for i in collection.find().sort("name",{"_id":0}):
            print(i)
    elif user_input == 4:
        for i in collection.find({},{"_id":0}).sort("name",-1):
            print(i)
    admin()

def delete_data():
    user_input = input("Who you want to delete:")
    try:
        query = {"name":user_input}
        data = collection.find(query)
        if data is not None:
            for i in data:
                print(i)
            user_confirm = input("Are you sure to delete y or n:")
            if user_confirm == 'y':
                collection.delete_one(query)
                print("Deleted Successfully Complete!")
            else:
                delete_data()
        else:
            query = {"name":{"$regex":f"^{user_input}"}}
            datas = collection.find(query, {"_id": 0})
            if datas is not None:
                for i in datas:
                    print(i)
                user_comfirm = input("Are you sure to delete that data y or n:")
                if user_comfirm == 'y':
                    dataUpdate = collection.delete_many(datas)
                    print("Deleted Accounts",dataUpdate.deleted_count)
                else:
                    delete_data()
        admin()
    except Exception as err:
        print(err)



def insert_DB(data):
    try:
        obj = collection.insert_one(data)
        print("Data are successfully Inserted")
    except Exception as err:
        print(err)
def insert_Data(email:None):
    name = input("Enter Your Name:")
    age = input("Enter Your age:")
    if email ==None:
        email = input("Enter Your email:")
        password = input("Enter Your password:")
        dataFormat = {"name": name, "age": age, "email": email, "password": password}
        dataList.append(dataFormat)
        insert_DB(dataFormat)
        admin()
    else:
        password = input("Enter Your password:")
        dataFormat = {"name":name,"age":age,"email":email,"password":password}
        dataList.append(dataFormat)
        insert_DB(dataFormat)

if __name__ == "__main__":
    while True:
        main()
















