from django.contrib import admin
from .models import Task


admin.site.site_header = 'ToDo App'



admin.site.register(Task)