from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin


from .models import Post,Category,Review



class PostAdmin(SummernoteModelAdmin):
    list_display=['title','draft','category']
    search_fields=['title','content']
    list_filter=['draft']
    summernote_fields = ('content',)

admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Review)

