from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.utils import timezone

from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify


FLAG_TYPE=[
    ('New','New'),
    ('Sale','Sale'),
    ('Feature','Feature'),
]
class Product(models.Model):
    name=models.CharField(max_length=120)
    flag=models.CharField(max_length=25,choices=FLAG_TYPE)
    price=models.FloatField()
    image=models.ImageField(upload_to='image_product')
    sku=models.IntegerField()
    subtitle=models.TextField(max_length=5000)
    descriptions=models.TextField(max_length=50000)
    brand=models.ForeignKey('Brand',related_name='product_brand',on_delete=models.SET_NULL,null=True,blank=True)
    tags = TaggableManager()
    slug=models.SlugField(null=True,blank=True)
    quantity=models.FloatField()

    def __str__(self):
        return self.name
    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super(Product,self).save(*args,**kwargs)

    @property
    def count_review(self):
        reviews=self.review_product.all().count()
        return reviews
    
    @property
    def avg_rate(self):
        total=0
        reviews=self.review_product.all()
        if len(reviews) > 0:
            for item in reviews:
                total += item.rate
            avg=total/len(reviews)
        else:
            avg=0
        return avg



class Brand(models.Model):
    name=models.CharField(max_length=120)
    image=models.ImageField(upload_to='image_brand')
    slug=models.SlugField(null=True,blank=True)

    def __str__(self):
        return self.name
    
    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super(Brand,self).save(*args,**kwargs)

class Image_Product(models.Model):
    product=models.ForeignKey(Product,related_name='image_product',on_delete=models.CASCADE)
    images=models.ImageField(upload_to='images')

    def __str__(self):
        return str(self.product)

class Review(models.Model):

    user=models.ForeignKey(User,related_name='review_user_product',on_delete=models.CASCADE)
    product=models.ForeignKey(Product,related_name='review_product',on_delete=models.CASCADE)
    review=models.TextField(max_length=1500)
    publish_date=models.DateTimeField(default=timezone.now)
    rate=models.IntegerField(choices=[(i,i) for i in range(1,5)])

    def __str__(self):
        return f'{self.user}---{self.product}'

