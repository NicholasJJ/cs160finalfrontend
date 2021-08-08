from django.urls import path
from . import views

urlpatterns = [
    path('gallery', views.gallery, name='gallery'),
    path('testwrite', views.testwrite, name='testwrite'),
    path('genre', views.genre, name='genre')
]
