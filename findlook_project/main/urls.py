from django.urls import path
from django.urls.resolvers import URLPattern
from main import views


urlpatterns = [
    path('', views.main_index, name='main'),
]