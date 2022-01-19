from django.urls import path
from closet import views


app_name = 'closet'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]