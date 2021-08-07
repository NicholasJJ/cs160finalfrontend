from django.urls import path
from . import views

urlpatterns = [
    path('demo', views.demo, name='demo'),
    path('new_interaction', views.new_interaction, name='new_interaction'),
    path('home', views.home, name='home'),
    path('drawPad', views.drawPad, name='drawPad'),
    path('gallery', views.gallery, name='gallery'),
    path('colorPicker', views.colorPicker, name='colorPicker')
]
