from django.shortcuts import render
from rest_framework import  generics
from .models import EMSLogConfig
from .serializers import LogSerializer
# Create your views here.


class SyslogListView(generics.ListAPIView):
    serializer_class = LogSerializer
    queryset = EMSLogConfig.objects.all()