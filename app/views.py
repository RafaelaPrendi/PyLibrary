from django.shortcuts import render, get_object_or_404
from . import models
def libra(request, id):
    # "get_object_or_404"
    # Browserit / klientit i kthehet 404
    libri = get_object_or_404(models.Liber, pk=id)
    data = {
        'librat': [libri.as_dict()],
        'titulli_i_faqes': 'Libra (id: {})'.format(id),
        'variabla_ime' : False
    }
    return render(request, 'libra.html', data)