from django.contrib import admin

from . models import (
    Anemometer,
    AnemometerCategory, 
    WindReading, 
    Tags)

# Register your models here.
admin.site.register(Anemometer)
admin.site.register(AnemometerCategory)
admin.site.register(WindReading)
admin.site.register(Tags)