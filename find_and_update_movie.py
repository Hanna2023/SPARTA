from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta 

matrix_star = db.movies.find_one({'title' : '매트릭스'})['star']

movies_with_matrix_star = list(db.movies.find({'star' : matrix_star}))

for movie in movies_with_matrix_star:

    print(movie['title'])

    db.movies.update_many(
        {'star' : matrix_star},
        {
            '$set' : {'star' : 0}
        }
        )