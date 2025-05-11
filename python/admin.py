from django.contrib import admin
from .models import PythonInfo

@admin.register(PythonInfo)
class PythonInfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'created_at', 'updated_at')
    list_filter = ('created_by', 'created_at')
    search_fields = ('title', 'description')
    date_hierarchy = 'created_at'