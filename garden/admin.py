from django.contrib import admin
from .models import Garden, GardenType, Plant
# Register your models here.
admin.site.register(Garden)
admin.site.register(GardenType)
admin.site.register(Plant)