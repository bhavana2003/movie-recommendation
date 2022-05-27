from django import views
from django.urls import path

from . import views

# contains url/path connection 

urlpatterns = [
  path('',views.index, name='index'),
  path('searchbar/', views.searchbar, name='searchbar'),
  path('', views.home, name='home'),
  path('signup/', views.signup, name='signup'),
  path('register/', views.register, name='register'),
  path('signin/', views.signin, name='signin'),
  path('login/', views.login, name='login'),
  path('logout/', views.logout, name='logout')
]