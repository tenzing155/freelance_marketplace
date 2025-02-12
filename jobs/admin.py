from django.contrib import admin
from .models import Job  # <- This is what registers the Job model in admin

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'budget', 'posted_by', 'created_at')
    search_fields = ('title', 'posted_by__username')
