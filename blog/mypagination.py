from rest_framework.pagination import PageNumberPagination

class MyPag(PageNumberPagination):
    page_size=10