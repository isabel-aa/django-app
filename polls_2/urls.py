""" Modulo para definicao de rotas do app"""
from django.urls import path
from .views import index, isabel, maria, maria_two, conversor, PrimeiraCBView, SegundoConversor

# URLS Config do app
# Define a relacao entre um path e uma view
urlpatterns = [
   path('', index, name='index_polls_2'),

   # 2. Definir a url
   path('isabel/', isabel, name='isabel_view'),

    # 2. Definir a url
    path('maria/', maria, name='maria_view'),

    path('casa/maria/', maria_two, name='maria_two'),

    # 2. Cadastro a url
    path('conversor/', conversor, name='conversor'),

    # 2. Cadastro a url
    path('conversor-cbv/', PrimeiraCBView.as_view(), name='conversor_cbv'),

    #2. Cadastro a url
    path('conversor_new/', SegundoConversor.as_view(), name='conversor_new'),
]
