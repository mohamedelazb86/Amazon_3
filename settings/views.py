from django.shortcuts import render
from product.models import Product,Brand,Review
from django.db.models import Count

def home(request):

    brand=Brand.objects.all()[:10].annotate(product_count=Count('product_brand'))
    sale_product=Product.objects.filter(flag='Sale')[:10]
    new_product=Product.objects.filter(flag='New')[:10]
    feature_product=Product.objects.filter(flag='Feature')[:6]
    sale_product=Product.objects.filter(flag='New')[:10]

    reviews=Review.objects.all()[:10]

    context={
        'brand':brand,
        'sale_product':sale_product,
        'new_product':new_product,
        'feature_product':feature_product,
        'reviews':reviews
    }


    return render(request,'settings/home.html',context)