from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('gallery1/', views.ArticleGallery1View.as_view()),
    path('gallery2/', views.ArticleGallery2View.as_view()),
    path('gallery1/<article_id>/', views.ArticleGallery1View.as_view()),
    path('gallery2/<article_id>/', views.ArticleGallery2View.as_view()),
]