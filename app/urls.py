from django.urls import path
from . import views

urlpatterns = [
    # path(<url_qe_vjen_si_kerkese>, <funksioni qe do ekzekutohet>)
    path(r'home/', views.index, name='index'),
    path('accounts/login/', views.Login, name='Login'),
    path('accounts/register/', views.register, name='register'),
    path('accounts/logout/', views.Logout, name='Logout'),
    path(r'libra/<int:id>/', views.libra, name='libra'),
    path(r'autore/<int:id>/', views.autore, name='autore'),
    path(r'shto_liber/', views.shto_liber, name='shto_liber'),
    path(r'hiq_liber/', views.hiq_liber, name='hiq_liber'),
    path(r'libratemi/', views.librat_e_mi, name='librat_e_mi'),
    path(r'results/', views.search, name='search'),
    path(r'rating/', views.get_rating, name='get_rating'),
]
