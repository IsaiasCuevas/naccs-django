from django.urls import path

from . import views

urlpatterns = [
    path(r'powerpugs/', views.powerpugs, name='power_pugs'),
    path(r'powerpugs/application', views.application, name="pp_player_app"),
    path(r'powerpugs/application/igl', views.iglapplication, name="pp_igl_app")
    
]
