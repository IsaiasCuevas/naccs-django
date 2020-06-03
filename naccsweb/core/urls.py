from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('riot.txt', views.riot, name="riot")
]