from app.models import Liber
import csv
def krijo_liber(autori, titulli, img_src, _id):
    cmimi = "15.00 EUR"
    liber = Liber(
        titulli=titulli,
        autori=autori,
        cmimi=cmimi,
        img_src=img_src,
        _id=_id
    )
    liber.save()
def krijo_librat():
    with open('scripts/books.csv', 'r') as data:
        reader = csv.reader(data)
        for rrjesht in reader:
            autori = rrjesht[7]
            titulli = rrjesht[9]
            img_src = rrjesht[-2]
            _id = rrjesht[0]
            krijo_liber(
                autori,
                titulli,
                img_src, _id
            )
def numri_i_librave():
    return Liber.objects.all().count()

def run():
    print('Numri para:', numri_i_librave())
    krijo_librat()
    print('Numri pas:', numri_i_librave())

def numri_i_librave():
    return Liber.objects.all().count()
    print('here')