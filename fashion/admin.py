from django.contrib import admin
from .models import Trends

# Register your models here.
@admin.register(Trends)
class TrendsAdmin(admin.ModelAdmin):
    list_display = ('Style','colors','number_of_pieces')