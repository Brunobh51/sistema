from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name='dashboard'),
    path("cotacao/", views.cotacao, name='cotacao'),
    path("entregas/", views.lista_entregas, name='entregas' ),
    path("formulario/", views.formulario, name='formulario')

    # Outras URLs relacionadas à cotação de entregas podem ser adicionadas aqui
]
