from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('gallery1/', views.ArticleGallery1View.as_view()),
    path('gallery2/', views.ArticleGallery2View.as_view()),
    path('comment/', views.CommentView.as_view()),
    path('comment/<comment_id>', views.CommentView.as_view()),

]