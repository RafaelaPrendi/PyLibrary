import csv
from app.models import Liber, Autor, Rating
from django.contrib.auth.models import User


def krijo_rating(user, liber, rating):
    rating = Rating(
        user=user,
        liber=liber,
        rating=rating
    )
    rating.save()

def krijo_lidhje(user_id, book_id, rating):
    libri = Liber.objects.filter(iid=book_id)
    user = User.objects.get(id=user_id)
    rating = Rating.objects.filter(rating=rating)
    # <fusha>.add(<objekti>)
    rating.liber.add(libri)
    rating.user.add(user)
    # <objekti>.save() -> ben qe ndryshimet te jene ne databaze
    rating.save()
def krijo_ratings():
    with open('ratings.csv', 'r', encoding='utf8') as data:
        reader = csv.reader(data)
        for rrjesht in reader:
            user_id = rrjesht[0]
            book_id = rrjesht[1]
            rating = rrjesht[2]
            krijo_rating(user_id, book_id, rating)


def krijo_lidhjet():
    with open('ratings.csv', 'r', encoding='utf8') as data:
        reader = csv.reader(data)
        for rrjesht in reader:
            user_id = rrjesht[0]
            titulli = rrjesht[1]
            rating = rrjesht[2]
            krijo_lidhje(user_id, titulli, rating)
def zbraz():
    Rating.objects.all().delete()

def numri_i_rating():
    return Rating.objects.all().count()

def run():
    print("Pastrim i DB ...")
    zbraz()
    print('Krijo rating ...')
    print('(Rating) Numri para:', numri_i_rating())
    print('(Rating) Numri pas:', numri_i_rating())
    krijo_lidhjet()

