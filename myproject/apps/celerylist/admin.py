from django.contrib import admin

from .models import Celery, list


admin.site.register(Celery)
admin.site.register(list)