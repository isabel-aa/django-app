""" Modulo para definicao de rotas do app"""
from django.urls import path
from .views import index, isabel, maria, maria_two, conversor, PrimeiraCBView, SegundoConversor, IndexView, \
    TemplateView, ConversorSuperPower, update_categoria, \
    delete_categoria, ListaCategoria, DetailCategoria, CreateCategoria

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

    # 2. Cadastro url
    path('index_new/', IndexView.as_view(), name='index_new'),

    # 3. Renderizando um template directamente.
    path('index_refactor/', TemplateView.as_view(template_name='index.html'), name='index_refactor'),

    # 2. url
    path('power_conversor/', ConversorSuperPower.as_view(), name='power_conversor'),

    # 2.
    path('categorias/', ListaCategoria.as_view(), name='lista_categorias'),

    path('categorias/new/', CreateCategoria.as_view(), name='create_categoria'),

    # 2. URL com parametros

    path('categorias/<int:id>/', DetailCategoria.as_view(), name='detail_categoria'),

    # 2. URL Com parametros
    path('categorias/<int:id>/update/', update_categoria, name='update_categoria'),

    # 2. URL Com parametros
    path('categorias/<int:id>/delete/', delete_categoria, name='delete_categoria'),
]

