from django.shortcuts import render
from rest_framework import viewsets
from .models import Buku
from .serializers import BukuSerializer


# Create your views here.

class BukuView(viewsets.ModelViewSet):
    queryset = Buku.objects.all()
    serializer_class = BukuSerializer
