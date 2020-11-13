import csv, random
from app.models import Liber, Autor, Profil, Rating
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.core.exceptions import ObjectDoesNotExist


def krijo_rating(user_id, book_id, rating):
    #user, liber, rating
    random_username = get_random_string(length=5, allowed_chars='asdfghjklqwertyuiopzxcvbnm')
    random_password = 'django1234'
    try:
        user = User.objects.get(id=user_id)
    except ObjectDoesNotExist:
        user = User.objects.create_user(username=random_username, password=random_password)

    lib = Liber.objects.get(iid=book_id)
    rating = Rating.objects.create(user=user, liber=lib, rating=rating)
    rating.save()

def krijo_ratings():
     with open('ratings.csv', 'r', encoding='utf8') as data:
         reader = csv.reader(data)
         for rrjesht in reader:
             user_id = rrjesht[0]
             book_id = rrjesht[1]
             rating = rrjesht[2]
             krijo_rating(user_id, book_id, rating)
# to create random ratings
#def krijo_ratings():
    #user, liber, rating
    #user = User.objects.all()
    #user_count = User.objects.all().count() - 1
    #librat= Liber.objects.all()
    #for lib in librat:
        #rating = Rating(
                #user=user[random.randint(0, user_count)],
        #         user=user,
        #         liber=lib,
        #         rating=rating
        #         )
        # rating.save()

def run():
    print("pastrimi i db")
    Rating.objects.all().delete()
    print("Numri i rating para: ", Rating.objects.all().count())

    krijo_ratings()
    print("Numri i rating pas: ", Rating.objects.all().count())

