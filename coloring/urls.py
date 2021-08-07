from django.urls import path
from . import views
from . import BackendMySQL

urlpatterns = [
    path('gallery', views.gallery, name='gallery'),
    path('testwrite', views.testwrite, name='testwrite'),
    path('index', views.index, name='index'),
    path('test_api', BackendMySQL.test_api, name='test_api'),
    path('login', BackendMySQL.login, name='login'),
    path('register', BackendMySQL.register, name='register'),
    path('uploadText', BackendMySQL.uploadText, name = "uploadText"),
    path('getText', BackendMySQL.getText, name = "getText"),
]
