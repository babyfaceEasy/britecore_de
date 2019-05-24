from django.shortcuts import render
from rest_framework import generics

from . import serializers
from . import models

# Create your views here.


class InusrerListView(generics.ListCreateAPIView):
    queryset = models.Insurer.objects.all()
    serializer_class = serializers.InsurerSerializer
