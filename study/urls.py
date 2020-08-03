from django.urls import path
from study import views

urlpatterns = [
    # path('add_day', views.add_day),
    path('get_days', views.get_days),
    path('add_day', views.add_day),
    path('edit_day', views.edit_day),
    path('get_students', views.get_student),
    path('get_comment', views.get_comment),
    path('add_comment', views.add_comment),
]
