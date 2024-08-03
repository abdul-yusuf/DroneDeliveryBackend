from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Drone)
admin.site.register(models.Flight)