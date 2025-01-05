from django.contrib import admin
from .models import Gadgets

# Register your models here.
@admin.register(Gadgets)
class GadgetsAdmin(admin.ModelAdmin):
    list_display = ('model_name','model_type','model_cost')