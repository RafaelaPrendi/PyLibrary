from django.db import models

# Create your models here.
class Liber(models.Model):
    titulli = models.CharField(max_length=255)
    autori = models.CharField(max_length=255)
    cmimi = models.CharField(max_length=255)
    img_src = models.CharField(max_length=255)
    _id = models.IntegerField(primary_key=True)

    def as_dict(self):
        return {
            "titulli": self.titulli,
            "autori": self.autori,
            "cmimi": self.cmimi,
            "img_src": self.img_src
        }
    # modeli per autoret
class Autor(models.Model):
    emri = models.CharField(max_length=255)
    _id = models.IntegerField(primary_key=True)

    def as_dict(self):
        return {
            'emri' : self.emri
        }