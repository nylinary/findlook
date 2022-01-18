from django.urls import path
from django.urls.resolvers import URLPattern
from main import views


# Template tagging
app_name = 'main'

urlpatterns = [
    path('', views.WebpageListView.as_view(), name='main'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('<int:pk>/', views.WebpageDetailView.as_view(), name='detail'),
]