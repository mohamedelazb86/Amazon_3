from django.urls import path
from . import views,api


app_name='product'

urlpatterns = [
    
    # brand
    path('brands',views.Brand_List.as_view()),
    path('brands/<slug:slug>',views.Brand_Detail.as_view()),

    #product
    path('',views.Product_List.as_view()),
    path('<slug:slug>',views.Product_Detail.as_view()),
    path('product/<slug:slug>',views.add_review,name='add-review'),

    # api
    path('product/api/api',api.ProductApi.as_view()),
    path('product/api/api/<int:pk>',api.ProductDetailApi.as_view()),
    
    
]
