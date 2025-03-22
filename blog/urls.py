from django.urls import path
from . import views

app_name='blog'
urlpatterns = [
    path('',views.posts,name='posts'),
    path('<slug:slug>',views.post_detail,name='post-detail'),
    path('<slug:slug>/delete',views.post_delete,name='post-delete'),
    path('<slug:slug>/udate',views.update_post,name='post-update'),
]
