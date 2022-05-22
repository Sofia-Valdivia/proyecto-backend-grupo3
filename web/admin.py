from django.contrib import admin

# Register your models here.
from .models import Region,Tours

admin.site.register(Region)
admin.site.register(Tours)
