from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name='dashboard'),
    path("cotacao/", views.cotacao, name='cotacao'),

    # Outras URLs relacionadas à cotação de entregas podem ser adicionadas aqui
]
