from django.db import models
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    user = models.ForeignKey('user.User', verbose_name="작성자", on_delete=models.SET_NULL, null=True)
    title = models.CharField("제목", max_length=50)
    category = models.ForeignKey(Category, verbose_name="카테고리",on_delete=models.SET_NULL, null=True)
    img_url = models.CharField("img_url", max_length=200)
    created_at = models.DateTimeField("만든 날", auto_now_add=True)
    updated_at = models.DateTimeField("업데이트 한 날", auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey('user.User',verbose_name="작성자",on_delete=models.CASCADE)
    article = models.ForeignKey(Article,verbose_name="게시글",on_delete=models.CASCADE)
    content = models.TextField("댓글")
    created_at = models.DateTimeField("댓글 작성 일", auto_now_add=True)
    updated_at = models.DateTimeField("업데이트 일", auto_now=True)    

    def __str__(self):
        return f'id [ {self.id} ] {self.article.title} : {self.content} / {self.user.username}님이 작성한 댓글'