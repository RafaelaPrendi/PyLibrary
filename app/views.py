from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from . import models
from django.views.generic import  ListView

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

@login_required(login_url='/accounts/login/')
@require_http_methods(["POST"])
def librat_e_mi(request):
    user = request.user
    data = {}
    return render(request, 'libra.html', data)

from .forms import HiqLiberForm, ShtoLiberForm

@login_required(login_url='/accounts/login/')
@require_http_methods(["POST"])
def shto_liber(request):
    data = {}
    return render(request, 'libra.html', data)

@login_required(login_url='/accounts/login/')
@require_http_methods(["POST"])
def hiq_liber(request):
    data = {}
    return render(request, 'libra.html', data)

# view funct for home page
@require_http_methods(["GET"])
def index(request):
    nr_librave = models.Liber.objects.all().count()
    nr_profil = models.Profil.objects.all().count()
    nr_autoreve = models.Autor.objects.count()
    data = {
        'nr_librave' : nr_librave,
        'nr_profil' : nr_profil,
        'nr_autoreve' : nr_autoreve
    }
    return render(request, 'index.html', data)

@require_http_methods(["GET"])
def search(request):
    if request.GET.get('searchForm'):
        searchItem = request.GET.get('q')
        try:
            book = models.Liber.objects.filter(titulli__icontains=searchItem)
            return render(request, 'results.html', {"Books": book})
        except:
            return render(request, 'results.html', {"Books": book})
    else:
        return render(request, 'results.html', {})

