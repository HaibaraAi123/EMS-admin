from rest_framework import serializers
from .models import EMSLogConfig


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = EMSLogConfig
        fields = '__all__'
