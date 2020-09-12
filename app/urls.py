from django.urls import path
from . import views

urlpatterns = [
    # path(<url_qe_vjen_si_kerkese>, <funksioni qe do ekzekutohet>)
    path(r'libra/<int:id>/', views.libra, name='libra'),
    path(r'autore/<int:id>/', views.autore),
    path(r'libratemi/', views.librat_e_mi, name='librat_e_mi'),
    path(r'shto_liber/', views.shto_liber, name='shto_liber'),
    path(r'hiq_liber/', views.shto_liber, name='hiq_liber'),
    path(r'home/', views.index, name='index'),
    path(r'results/', views.search, name='search'),
]
