from django.urls import path
from main import views
from .views import *


# Template tagging
app_name = 'main'

urlpatterns = [
    # path('', views.WebpageListView.as_view(), name='main'),
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    # path('<int:pk>/', views.WebpageDetailView.as_view(), name='detail'),
    path('about/', views.AboutView.as_view(), name='about'),
]