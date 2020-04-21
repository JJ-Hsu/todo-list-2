from django.contrib import admin
from . models import Task


class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_complete', 'date')

# Register your models here.
admin.site.register(Task, TodoAdmin)
