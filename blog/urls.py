from django.urls import path
from . import views
from . import api

app_name='blog'
urlpatterns = [
    path('',views.posts,name='posts'),
    path('<slug:slug>',views.post_detail,name='post-detail'),
    path('<slug:slug>/delete',views.post_delete,name='post-delete'),
    path('<slug:slug>/udate',views.update_post,name='post-update'),

    # api

    path('posts/api',api.PostApi.as_view()),
    path('post/detail/api/<int:pk>',api.PostDetailApi.as_view()),
]
