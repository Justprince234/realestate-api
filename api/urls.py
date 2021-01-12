from django.urls import path

from realtors.views import ListRealtor
from listings.views import ListSale, DetailSale, ListRent, DetailRent, SaleSearchAPIView, RentSearchAPIView
from contacts.views import SaleContactList, RentContactList
from accounts.views import RegisterView

urlpatterns = [
    path('sale/<int:pk>/', DetailSale.as_view()),
    path('Rent/<int:pk>/', DetailRent.as_view()),
    path('sales/', ListSale.as_view()),
    path('rents/', ListRent.as_view()),
    path('accounts/register/', RegisterView.as_view()),
    path('salecontact/', SaleContactList.as_view()),
    path('rentcontact/', RentContactList.as_view()),
    path('salesearch/', SaleSearchAPIView.as_view()),
    path('rentsearch/', RentSearchAPIView.as_view()),
    path('realtors/', ListRealtor.as_view()),
]