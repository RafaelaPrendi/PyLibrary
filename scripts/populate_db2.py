from app.models import Autor
import csv

def krijo_Autor(emri, _id):
    autor = Autor(
        emri = emri,
        _id=_id)
    autor.save()

def krijo_Autoret():
    with open('scripts/books.csv', 'r') as data:
        reader = csv.reader(data)
        for rresht in reader:
            emri = rresht[7]
            _id = rresht[0]
            krijo_Autor(emri, _id)

def numri_autoreve():
    return Autor.objects.all().count()

def run():
    print(" Numri para : ", numri_autoreve())
    krijo_Autoret()
    print(" Numri pas :", numri_autoreve())
