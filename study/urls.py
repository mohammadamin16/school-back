from django.urls import path
from study import views

urlpatterns = [
    # path('add_day', views.add_day),
    path('get_days', views.get_days),
    path('view2', views.view2),
]
