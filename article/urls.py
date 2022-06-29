from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('article/gallery1/', views.ArticleGallery1View.as_view()),
    path('article/gallery2/', views.ArticleGallery2View.as_view()),
]