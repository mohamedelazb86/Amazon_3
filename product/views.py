from django.shortcuts import render,redirect
from .models import Product,Image_Product,Review,Brand
from django.views.generic import ListView,DetailView
from django.db.models import Count

class Product_List(ListView):
    model=Product
    template_name='product/product_list.html'
    paginate_by=28

class Product_Detail(DetailView):
    model=Product
    template_name='product/product_detail.html'

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["images"] = Image_Product.objects.filter(product=self.get_object())
        context["reviews"] = Review.objects.filter(product=self.get_object())
        context["related"] = Product.objects.filter(brand=self.get_object().brand)
        return context
    
def add_review(request,slug):
    product=Product.objects.get(slug=slug)
    review=request.POST['rate']
    rate=request.POST['rating']

    Review.objects.create(
        product=product,
        user=request.user,
        review=review,
        rate=rate
    )
    return redirect(f'/products/{slug}')

class Brand_List(ListView):
    model= Brand
    template_name='product/brand_list.html'
    paginate_by=20
    queryset=Brand.objects.all().annotate(product_count=Count('product_brand'))

    

# class Brand_Detail(DetailView):
#     model=Brand
#     template_name='product/brand_detail.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["related"] = Product.objects.filter(brand=self.get_object())
#         return context

class Brand_Detail(ListView):
    model=Product
    template_name='product/brand_detail.html'
    paginate_by=10
    
    def get_queryset(self):
        brand=Brand.objects.get(slug=self.kwargs['slug'])
        queryset=super().get_queryset().filter(brand=brand)
        return queryset
    

    def get_context_data(self, **kwargs) :
    
        context = super().get_context_data(**kwargs)
        context["brand"] = Brand.objects.filter(slug=self.kwargs['slug']).annotate(product_count=Count('product_brand'))[0]
        return context
    
    


    


   

