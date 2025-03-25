from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Product,Review,Image_Product,Brand


class ImageAdmin(admin.TabularInline):
    model=Image_Product

class ProductAdmin(SummernoteModelAdmin):
    list_display=['name','flag','brand']
    list_filter=['brand']
    search_fields=['name','subtitle','descriptions']

    summernote_fields = ('subtitle','descriptions')
    
    inlines=[ImageAdmin]



admin.site.register(Product,ProductAdmin)
admin.site.register(Review)
admin.site.register(Image_Product)
admin.site.register(Brand)
