from django.urls import path

from . import views

urlpatterns = [
    path('', views.planet_name, name='index'),

]
