from django.db import models
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)


class Article(models.Model):
    # user_id = models.ForeignKey('user.User', verbose_name="작성자", on_delete=models.SET_NULL, null=True)
    title = models.CharField("제목", max_length=50)
    category = models.ForeignKey(Category, verbose_name="카테고리",on_delete=models.SET_NULL, null=True)
    img_url = models.CharField("img_url", max_length=200)
    created_at = models.DateTimeField("만든 날", auto_now_add=True)
    updated_at = models.DateTimeField("업데이트 한 날", auto_now=True)
