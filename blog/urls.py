from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('blog/',index,name="blog-index"),
    path('post_detail/<int:pk>/',post_detail,name='blog-post-detail'),
    path('post_edit/<int:pk>/',post_edit,name='blog-post-edit'),
        path('post_delete/<int:pk>/',post_delete,name='blog-post-delete'),

]