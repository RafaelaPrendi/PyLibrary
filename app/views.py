from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.messages import constants as messages
from django.contrib import auth
from django.contrib.auth import login, authenticate
from . import models
from .models import Liber, Autor, Profil, Rating
from django.contrib.auth.models import User
from .forms import HiqLiberForm, ShtoLiberForm, RatingForm
from django import forms
import random
from django.views.generic import  ListView
from django.contrib import messages

@require_http_methods(["GET"])
def libra(request, id):
    # "get_object_or_404"
    # Browserit / klientit i kthehet 404
    libri = get_object_or_404(models.Liber, pk=id)
    data = {
        'liber': libri,
        'titulli_i_faqes': 'Libra (id: {})'.format(id),
    }
    return render(request, 'libra.html', data)

@require_http_methods(["GET"])
def autore(request, id):
    autori = get_object_or_404(models.Autor, pk=id)

    data = {
        'titulli_i_faqes': '{}: {}'.format(id, autori.emri),
        'autori': autori.as_dict(),
        'librat': [lib.as_dict() for lib in autori.librat.all()]
    }
    return render(request, 'autore.html', data)

# view funct for home page
@require_http_methods(["GET"])
def index(request):
    nr_librave = models.Liber.objects.all().count()
    nr_profil = models.Profil.objects.all().count()
    nr_autoreve = models.Autor.objects.count()
    libri = list()
    for i in range(0,3):
        randnr = random.randint(1, nr_librave)
        query = models.Liber.objects.filter(iid=randnr)
        for lib in query:
            libri.append(lib.img_src)
    data = {
        'nr_librave' : nr_librave,
        'nr_profil' : nr_profil,
        'nr_autoreve' : nr_autoreve,
        'libri1' : libri[0],
        'libri2': libri[1],
        'libri3': libri[2],

    }
    return render(request, 'index.html', data)

def Login(request):
    if request.method == 'POST':
        form = AuthenticationForm()
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                request.session['user'] = user
                messages.info(request, f' You are now logged in as {{ username }}')
                return redirect('libratemi.html')
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    else:
        form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form': form})


def register(request):
    data = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request, user)
            request.session['user'] = user
            messages.info(request, f' You are now logged in as {{ username }}')
            return render(request, 'index.html')
    data['form'] = form
    return render(request, 'registration/register.html', data)

def Logout(request):
    auth.logout(request)
    return render(request, 'registration/logout.html')

############################
@login_required(login_url='/accounts/login/')
#@require_http_methods(["POST"])
def librat_e_mi(request):
    user = request.user
    profil = Profil.objects.get(user=user)
    librat = profil.librat.all()
    data = {'profil': user,
            'libra': librat}
    return render(request, 'libratemi.html', data)


# shton librat te profil si liber i lexuar
@login_required(login_url='/accounts/login/')
@require_http_methods(['POST'])
def shto_liber(request):
    if request.method == 'POST':
        form = ShtoLiberForm(request.POST)
        if form.is_valid():
            liber_id = int(form.cleaned_data['liber_id'])
            current_user = request.user
            # krijo lidhje user, liber i lexuar tek profil
            usr = User.objects.get(username=current_user)
            lbr = Liber.objects.get(pk=liber_id)

            profil = Profil.objects.get(user=usr)
            profil.librat.add(lbr)
            profil.save()

            data = {'profil': profil.user,
                    'libra': [lib.titulli for lib in profil.librat.all()]
                    }
            return redirect('librat_e_mi')
        else:
            return render(request, 'libratemi.html', {"msg": "error"})
    else:
        form = ShtoLiberForm()
        return render(request, 'libra.html', form)


# heq librat nga profil
@login_required(login_url='/accounts/login/')
@require_http_methods(["POST"])
def hiq_liber(request):
    if request.method == 'POST':
        form = HiqLiberForm(request.POST)
        if form.is_valid():
            lbr_id = int(form.cleaned_data['lbr_id'])
            current_user = request.user

            #gjej lidhje user, liber i lexuar tek profil dhe fshije
            profili = Profil.objects.get(user=current_user)
            libri = Liber.objects.get(iid=lbr_id)
            profili.librat.remove(libri)

            return redirect('librat_e_mi')
        else:
            return render(request, 'libratemi.html', {"msg": 'fucking error'})
    else:
        form = HiqLiberForm()
        return render(request, 'libra.html', form)

    data = {}
    return render(request, 'libra.html', data)


@require_http_methods(["GET"])
def search(request):
        request.GET.get('searchForm')
        searchItem = request.GET.get('q')
        book = Liber.objects.filter(titulli__icontains=searchItem)
        author = Autor.objects.filter(emri__icontains=searchItem)
        if book.count() != 0:
            return render(request, 'results.html', {"Books": book})
        else:
            if author.count() != 0:
                return render(request, 'results.html', {"Authors": author})
            else:
                return render(request, 'results.html', {'Books': 'Not Found in Database'})


@login_required(login_url='/accounts/login/')
@require_http_methods(["GET"])
def get_rating(request):
    form = RatingForm(request.GET.get('ratingForm'))
    rate_value = float(request.GET.get('rating'))
    current_user = request.user
    liber_id = request.GET.get('lbr_id')
    # add rating to rating table
    rating = Rating.objects.update_or_create(
        user=current_user,
        liber=Liber.objects.get(iid=liber_id),
        rating=rate_value
    )[0]
    rating.save()
    data = {'rate_val': rate_value}
    #return render(request, 'rating.html', data)
    return redirect('librat_e_mi')

from .recommend import get_recommends
@login_required(login_url='/accounts/login/')
def recommend(request):
    current_user = request.user
    current_user_ratings = []

    # get ratings from this user in form of list of tuples
    ratings = Rating.objects.filter(user=current_user)
    for rating in ratings:
        current_user_ratings.append((str(rating.liber.titulli), float(rating.rating)))

    # pass ratings to get_recommends
    recommendations = get_recommends(user_ratings=current_user_ratings)
    liber_id = []
    for titull in recommendations.keys():
            liber_obj = Liber.objects.filter(titulli=titull)[0]
            liber_id.append(liber_obj)

    recommendations = dict(zip(recommendations.keys(), liber_id))
    data = {'recommendations': recommendations,
            'user': current_user,
            }
    return render(request, 'rekomandime.html', data)


