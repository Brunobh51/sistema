from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include('app_CotacaoEntregas.urls')),
    path("admin/", admin.site.urls),
]
