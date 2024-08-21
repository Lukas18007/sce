from django.shortcuts import render
from rest_framework import generics
from business.models import Business
from business.serializers import BusinessSerializer

class BusinessCreateView(generics.ListCreateAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

class BusinessRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer