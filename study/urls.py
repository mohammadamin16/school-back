from django.urls import path
from study import views

urlpatterns = [
    path('get_days', views.get_days),
]
