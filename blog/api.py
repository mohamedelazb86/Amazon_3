# functions
from .serailizers import PostSerializers
from rest_framework import generics
from .models import Post
from .mypagination import MyPag
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class PostApi(generics.ListAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializers
    pagination_class=MyPag
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['draft', 'category']
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

class PostDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializers