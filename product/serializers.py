# form

from rest_framework import serializers
from .models import Product,Brand,Image_Product,Review


class ReviewproductSerializers(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields='__all__'

class ImageSerializers(serializers.ModelSerializer):
    class Meta:
        model=Image_Product
        fields='__all__'

class ProductSerializers(serializers.ModelSerializer):
    brand=serializers.StringRelatedField()
    class Meta:
        model=Product
        fields='__all__'

class ProductDetailSerializers(serializers.ModelSerializer):
    brand=serializers.StringRelatedField()
    images=ImageSerializers(source='image_product',many=True)
    review=ReviewproductSerializers(source='review_product',many=True)
    class Meta:
        model=Product
        # fields='__all__'
        fields=['name','flag','brand','images','review']

class BrandSerializers(serializers.ModelSerializer):
    class Meta:
        model=Brand
        fields='__all__'

class BrandDeatilSerializers(serializers.ModelSerializer):
    class Meta:
        model=Brand
        fields='__all__'


