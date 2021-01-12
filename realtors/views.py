from rest_framework import generics

from realtors.models import Realtor
from realtors.serializers import RealtorSerializer

# Create your views here.

class ListRealtor(generics.ListAPIView):
    queryset = Realtor.objects.filter(is_mvp=True)
    serializer_class = RealtorSerializer