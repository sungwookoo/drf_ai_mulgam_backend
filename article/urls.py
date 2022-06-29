from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('article/', views.ArticleGallery1View.as_view()),
]