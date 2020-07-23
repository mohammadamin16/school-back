from django.urls import path
from accounts import views

urlpatterns = [
    path('welcome', views.welcome),
    path('signup', views.signup),
    path('login', views.login),

]
