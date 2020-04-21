from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from tasks import views as tasks_views
from rest_framework import routers

router = routers.DefaultRouter()                      # add this
router.register(r'todos', tasks_views.TodoView, 'todo')     # add this

urlpatterns = [
    path('admin/', admin.site.urls),         path('api/', include(router.urls))                # add this
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
