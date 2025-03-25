#function
from . import serializers,mypaginations
from rest_framework import generics
from .models import Product,Brand



class ProductApi(generics.ListAPIView):
    queryset=Product.objects.all()
    serializer_class=serializers.ProductSerializers
    pagination_class=mypaginations.MyPagination

class ProductDetailApi(generics.RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=serializers.ProductDetailSerializers

class BrandApi(generics.ListAPIView):
    queryset=Brand.objects.all()
    serializer_class=serializers.BrandSerializers


class BrandDetailApi(generics.RetrieveAPIView):
    queryset=Brand.objects.all()
    serializer_class=serializers.BrandDeatilSerializers