from django.contrib import admin
from django.urls import path

from eventos import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("eventos", views.lista_eventos),
    path("eventos/<int:id>", views.detalhe_evento),
]