from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


# View: Funcoes
# signature: (request: Object) -> HttpResponse
#from django.urls import reverse, reverse_lazy


def index(request):
    return HttpResponse('<h1>Hola</h1>')


# 1. View: SEMPRE PRECISA RETORNAR UM HttpResponse
def isabel(request):
    return HttpResponse('<h1>isabel solicitou</h1>')


# 1. View
def maria(request):
    name = "bel"
    cores = [
        "azul",
        "verde",
        "vermelho",
    ]
    return render(request=request, template_name='index.html', context={'name': name, 'cores': cores})


# render é um shortcut
from django.template import loader
from .forms import LoginForm
# 1 View.
# DIY: Don't Repeat Yourself
def maria_two(request):
    name = "bel"
    cores = [
        "azul",
        "verde",
        "vermelho",
    ]
    form = LoginForm()
    response = loader.render_to_string(
        template_name='index.html',
        context={'name': name, 'cores': cores, 'form': form},
        request=request,
    )
    return HttpResponse(response)