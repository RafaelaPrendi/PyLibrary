from app.models import Liber, Autor, Profil, Rating
from django.contrib.auth.models import User
import csv
def get_csv():
    ratings = Rating.objects.all()
    with open('ratings.csv', 'w+', encoding='utf8') as data:
        writer = csv.writer(data)
        for rating in ratings:
            writer.writerow([rating.user.id, rating.liber.titulli, rating.rating])

def run():
    print(" CSV functions ")
    get_csv()