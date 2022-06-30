from rest_framework import serializers
from .models import Category, Article, Comment


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["name"]


class ArticleSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()


    def get_category(self, obj):
        return [category.name for category in obj.category.all()]

    class Meta:
        model = Article
        # fields = ["user","title","category","img_url"]
        fields = ["title","category","img_url"]

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"