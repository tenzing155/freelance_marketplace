from rest_framework import serializers
from .models import Job

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['id', 'title', 'description', 'budget', 'posted_by']  # Ensure 'posted_by' is listed
        extra_kwargs = {'posted_by': {'read_only': True}}  # ✅ This makes 'posted_by' automatic
