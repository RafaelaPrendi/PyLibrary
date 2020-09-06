from django.urls import path
from . import views

urlpatterns = [
    # path(<url_qe_vjen_si_kerkese>, <funksioni qe do ekzekutohet>)
    path(r'libra/<int:id>/', views.libra),
    path(r'autoret/<int:id>/', views.autoret),
]
