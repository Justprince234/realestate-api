from rest_framework import generics

from contacts.models import SaleContact, RentContact
from contacts.serializers import SaleContactSerializer, RentContactSerializer

# Create your views here.

class SaleContactList(generics.ListCreateAPIView):
    queryset = SaleContact.objects.all()
    serializer_class = SaleContactSerializer

class RentContactList(generics.ListCreateAPIView):
    queryset = RentContact.objects.all()
    serializer_class = RentContactSerializer