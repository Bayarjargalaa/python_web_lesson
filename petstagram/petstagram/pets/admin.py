

# Register your models here.
from django.contrib import admin
from .models import Pet

# Photo model-ийг Admin дээр бүртгэх
@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name',  'slug')
