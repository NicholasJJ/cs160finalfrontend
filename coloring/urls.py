from django.urls import path
from . import views
from coloring import BackendMySQL

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
    path('test_api', BackendMySQL.test_api, name='test_api'),
    path('login', BackendMySQL.login, name='login'),
    path('register', BackendMySQL.register, name='register'),
    path('uploadText', BackendMySQL.uploadText, name = "uploadText"),
    path('replaceText', BackendMySQL.replaceText, name = "uploadText"),
    path('getText', BackendMySQL.getText, name = "getText"),
    path('getTokenByInfo', BackendMySQL.getTokenByInfo, name = "getTokenByInfo"),
    path('getTokenGallery', BackendMySQL.getTokenGallery, name = "getTokenGallery"),
    path('index', views.index, name='index'),
    path('language', views.language, name='language'),
    path('getAll', BackendMySQL.getAll, name = "getAll"),
    path('addLanguage', BackendMySQL.addLanguage, name = "addLanguage"),
    path('getLanguage', BackendMySQL.getLanguage, name="getLanguage"),
    path('eraseLanguage', BackendMySQL.eraseLanguage, name = "eraseLanguage")
]
