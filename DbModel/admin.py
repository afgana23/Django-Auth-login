from django.contrib import admin
from .models import Country
@admin.register(Country)
class countryadmin(admin.ModelAdmin):
    list_display=("id",'country_name')

# Register your models here.
