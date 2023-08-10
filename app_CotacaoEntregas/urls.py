from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name='dashboard'),
    path("cotacao/", views.cotacao, name='cotacao'),
    path("criar_cliente/", views.criar_cliente, name='criar_cliente')
    # Outras URLs relacionadas à cotação de entregas podem ser adicionadas aqui
]
