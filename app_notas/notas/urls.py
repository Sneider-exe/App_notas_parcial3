from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('eliminarnota/<id>/', views.eliminarnota, name='eliminarnota'),
    path('editarnota/<id>/', views.editarnota, name='editarnota'),
    path('vernota/<id>/', views.vernota, name='vernota'),
    path('registro/', views.registro, name='registro'),
    path('nuevanota/', views.nuevanota, name='nuevanota'),



]