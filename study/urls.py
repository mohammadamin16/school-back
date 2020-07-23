from django.urls import path
from study import views

urlpatterns = [
    path('get_data', views.get_days),
]
