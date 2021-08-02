from rest_framework import generics

from .models import City
from .serializers import CitySerializer
from django_filters.rest_framework import DjangoFilterBackend

class ListCity(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['country',]

class DetailCity(generics.RetrieveAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer