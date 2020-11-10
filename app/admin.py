from django.contrib import admin

from .models import Liber, Autor, Rating, Profil

admin.site.register(Liber)
admin.site.register(Autor)
admin.site.register(Rating)
admin.site.register(Profil)