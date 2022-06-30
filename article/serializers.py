from rest_framework import serializers
from .models import Category, Article


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["name"]


class ArticleSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.username

    def get_category(self, obj):
        return [category.name for category in obj.category.all()]

    def create(self, validated_data):

        article = Article(**validated_data)
        article.save()
        return article

    def update(self, instance, validated_data):
        # instance에는 입력된 object가 담긴다.
        instance.title = validated_data.title
        instance.save()
        return instance

    class Meta:
        model = Article
        fields = ["user", "title", "category", "img_url"]