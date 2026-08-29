from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *

# from rest_framework.authentication import BasicAuthentication
# from rest_framework.permissions import IsAuthenticated


# Create your views here.

class TurfLC(generics.ListCreateAPIView):
    queryset = Turf.objects.all()
    serializer_class = TurfSerializer


class TurfRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Turf.objects.all()
    serializer_class = TurfSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]