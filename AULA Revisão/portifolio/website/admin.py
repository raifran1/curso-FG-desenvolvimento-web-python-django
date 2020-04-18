from django.contrib import admin
from .models import Curriculo

# Register your models here.

@admin.register(Curriculo)
class CurriculoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'formacao']
    search_fields = ['nome']
    list_filter = ['formacao']
    list_per_page = 2