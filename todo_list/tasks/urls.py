from django.urls import path, re_path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.task_list, name="task_list"),
]
