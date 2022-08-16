from django.urls import path
from .views import primeira_view

# TEMOS que respeitar esse nome 'urlparrters'
urlpatterns = [
    path('', primeira_view, name='first_view')
    # Signature: path(<path: str>, <view: Funcao>, <nome: str>)
]