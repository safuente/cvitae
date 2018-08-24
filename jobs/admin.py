from django.contrib import admin

# Register your models here.

from jobs.models import Job
from blogs.models import Blog

admin.site.register(Job)
admin.site.register(Blog)
