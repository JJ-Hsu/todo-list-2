from django.contrib import admin
from django.urls import path, include
from tasks import views as tasks_views
from rest_framework import routers

router = routers.DefaultRouter()                      
router.register(r'todos', tasks_views.TodoView, 'todo')     

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

