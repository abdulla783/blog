from django.contrib import admin
from django.urls import path
from blog.views import blogHome, blogPost

urlpatterns = [
    path('', blogHome, name='blgHome'),
    path('<str:slug>/', blogPost, name='blogPost'),
]