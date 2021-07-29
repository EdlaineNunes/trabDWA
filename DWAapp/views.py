from django.shortcuts import render
from DWAapp.models import *

# Create your views here.
def index(request):
    produtos = Produto.objects.all()

    context = {
        'produtos' : produtos,
    }
    return render(request, 'index.html', context)

def produto(request, id):
    produto = Produto.objects.get(id=id)
    context = {

        'produto': produto

    }
    return render(request, 'produto.html', context)