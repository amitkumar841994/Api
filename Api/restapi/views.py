from django.shortcuts import render
from rest_framework import viewsets
from restapi.models import student
from restapi.serializers import studentserializer
# Create your views here.

class studentviewset(viewsets.ModelViewSet):
    queryset =student.objects.all()
    serializer_class=studentserializer
    
