from django.urls import path
from . import views

urlpatterns = [
    path('gallery', views.gallery, name='gallery'),
    path('preview', views.preview, name='preview'),
    path('add_story', views.add_story, name='add_story'),
    path('write_summary', views.write_summary, name='write_summary'),
    path('view_book', views.view_book, name='view_book'),
    path('testwrite', views.testwrite, name='testwrite'),
    path('landing', views.landing, name='landing'),
    path('genre', views.genre, name='genre'),
    path('instructions', views.instructions, name='instructions'),
    path('language', views.language, name='language')
]
