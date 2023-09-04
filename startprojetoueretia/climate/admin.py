from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Forecast


admin.site.register(Forecast)


