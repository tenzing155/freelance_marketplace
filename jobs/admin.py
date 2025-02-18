from django.contrib import admin
from .models import Job, Bid  # ✅ Added Bid model

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'budget', 'client', 'created_at')  # ✅ Replaced 'posted_by' with 'client'
    search_fields = ('title', 'client__username')  # ✅ Updated 'posted_by__username' to 'client__username'

@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    list_display = ('job', 'freelancer', 'amount', 'created_at')
    search_fields = ('job__title', 'freelancer__username')  # ✅ Allow search by job title & freelancer username
