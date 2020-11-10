import csv, random
from app.models import Liber, Autor, Profil, Rating
from django.contrib.auth.models import User

def krijo_ratings():
    #user, liber, rating
    user = User.objects.all()
    user_count = User.objects.all().count() - 1
    librat = Liber.objects.all()
    for lib in librat:
            rating = Rating(
                user=user[random.randint(0, user_count)],
                liber=lib,
                rating=round(random.uniform(0, 5), 2)
            )
            rating.save()

def run():
    print("pastrimi i db")
    Rating.objects.all().delete()
    print("Numri i rating para: ", Rating.objects.all().count())

    krijo_ratings()
    print("Numri i rating pas: ", Rating.objects.all().count())
    print(User.objects.all().count())

