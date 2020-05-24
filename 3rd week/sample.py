#same as from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost:27017',27017)
db = client.spartadb

#collection
# db.users.insert_one({'name': 'bob', 'age': 21})
# db.users.insert_one({'name': 'job', 'age': 22})
# db.users.insert_one({'name': 'mary', 'age': 23})
#users can be written as people too; no se importa

# all_users = list(db.users.find())
# print(all_users)

# age_with_21 = list(db.users.find({'age' : 21}))
# print(age_with_21)
users_with_21_age = list(db.users.find({'age' : 21}))
# for user in users_with_21_age:
#     print(user['name'], user['age'])



db.users.update_many(
    {'age' : 21}, 
    {
        '$set' : {'age' : 22}
    }
    )
# update_many or update_one --> there are many types.. google it