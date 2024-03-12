from django.contrib import admin
from .models import Vegetable


# Register your models here.
@admin.register(Vegetable)
class VegetableAdmin(admin.ModelAdmin):
    list_display = ["name", "blocked"]
