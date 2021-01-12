from rest_framework import generics
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination


from listings.models import Sale, Rent
from listings.serializers import SaleSerializer, RentSerializer

# Create your views here.
class ListSale(generics.ListAPIView):
    queryset = Sale.objects.filter(is_published=True)
    serializer_class = SaleSerializer
    pagination_class = PageNumberPagination

class DetailSale(generics.RetrieveAPIView):
    queryset = Sale.objects.filter(is_published=True)
    serializer_class = SaleSerializer

class ListRent(generics.ListAPIView):
    queryset = Rent.objects.filter(is_published=True)
    serializer_class = RentSerializer
    pagination_class = PageNumberPagination

class DetailRent(generics.RetrieveAPIView):
    queryset = Rent.objects.filter(is_published=True)
    serializer_class = RentSerializer

class SaleSearchAPIView(generics.ListAPIView):
    queryset = Sale.objects.filter(is_published=True)
    serializer_class = SaleSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['city', 'bedrooms', 'state']

class RentSearchAPIView(generics.ListAPIView):
    queryset = Rent.objects.filter(is_published=True)
    serializer_class = RentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['city', 'bedrooms', 'state']