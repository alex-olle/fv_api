from django.contrib import admin
from .models import Month


# Register your models here.
@admin.register(Month)
class MonthAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "number"]
