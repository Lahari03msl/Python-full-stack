from django.contrib import admin
from .models import Items

# Register your models here.
@admin.register(Items)
class ItemsAdmin(admin.ModelAdmin):
    list_display = ('Name','Brand','cost')