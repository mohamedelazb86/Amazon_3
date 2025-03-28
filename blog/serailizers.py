# form
from rest_framework import serializers
from .models import Post,Review
from django.contrib.auth.models import User

class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields='__all__'
class UserSeializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

class PostSerializers(serializers.ModelSerializer):
    category=serializers.StringRelatedField()
    avg_count=serializers.SerializerMethodField()
    review=ReviewSerializers(source='review_post',many=True)
    user=UserSeializers()
    class Meta:
        model=Post
        fields='__all__'

    def get_avg_count(self,object):
        reviews=object.review_post.all().count()
        return reviews

class PostDetailSerializers(serializers.ModelSerializer):
    category=serializers.StringRelatedField()
    user=UserSeializers()
    avg_count=serializers.SerializerMethodField()
    class Meta:
        model=Post
        fields = '__all__'

    def get_avg_count(self,object):
        reviews=object.review_post.all().count()
        return reviews