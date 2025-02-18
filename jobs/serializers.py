from rest_framework import serializers
from .models import Job, Bid

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'
        read_only_fields = ['client']

class BidSerializer(serializers.ModelSerializer):
    freelancer = serializers.ReadOnlyField(source='freelancer.username')

    class Meta:
        model = Bid
        fields = '__all__'
        read_only_fields = ['freelancer', 'job']
