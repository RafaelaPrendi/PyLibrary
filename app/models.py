from django.db import models

# Create your models here.
class Liber(models.Model):
    titulli = models.CharField(max_length=255)
    autori = models.CharField(max_length=255)
    cmimi = models.CharField(max_length=255)
    img_src = models.CharField(max_length=255)
    iid = models.IntegerField(primary_key=True)

    def as_dict(self):
        return {
            "titulli": self.titulli,
            "autori": self.autori,
            "cmimi": self.cmimi,
            "img_src": self.img_src,
            "iid": self.iid
        }


class Autor(models.Model):
    emri = models.CharField(max_length=255)
    iid = models.IntegerField(primary_key=True)

    #<grumbull me libra qe i ka shkruajtur ky/kjo autor/e>
    librat = models.ManyToManyField(Liber)

    def as_dict(self):
        return {
            "emri": self.emri,
            "iid": self.iid
        }

# auth_models.User -> klase nga vete Django per menaxhimin e Users
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    librat = models.ManyToManyField(Liber)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profil.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profil.save()