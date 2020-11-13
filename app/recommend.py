import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from scipy import sparse
from .models import Liber, Autor, Rating
from django.contrib.auth.models import User

def get_recommends(user_ratings):

    def prepare_data():
        #ratings = pd.read_csv('ratings.csv')
        #books = pd.read_csv('books.csv')

        ratings = pd.DataFrame(list(Rating.objects.all().values()))
        books = pd.DataFrame(list(Liber.objects.all().values())).drop(['autori', 'cmimi', 'img_src'], axis=1)
        ratings = pd.merge(ratings, books, how='inner', left_on='liber_id', right_on='iid').drop('iid', axis=1)

        # ratings = pd.merge(books,ratings).drop(['drop1','drop2','drop3','drop4','drop5','drop6','drop7','drop8','drop9','drop10','drop11','drop12'
        #            ,'drop13','drop14','drop15','drop16','drop17','drop18','drop19','drop20','drop21'], axis=1)
        #ratings.head()
        userRatings = ratings.pivot_table(index=['user_id'], columns=['titulli'], values='rating')
        #userRatings.head()
        userRatings = userRatings.fillna(0, axis=1)

        corrMatrix = userRatings.corr(method='pearson')
        #corrMatrix.head()
        return corrMatrix

    def get_similar(book_title, rating, corrMatrix):
        similar_ratings = corrMatrix[book_title]*(rating-2.5)
        similar_ratings = similar_ratings.sort_values(ascending=False)
        return similar_ratings

    corrMatrix = prepare_data()

    similar_books = pd.DataFrame()
    for book, rating in user_ratings:
        similar_books = similar_books.append(get_similar(book, rating, corrMatrix), ignore_index=True)
    similar_books.head()
    return dict(similar_books.sum().sort_values(ascending=False).head(10))
