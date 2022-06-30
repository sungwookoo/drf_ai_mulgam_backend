from rest_framework import serializers
from .models import Category, Article


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["name"]


class ArticleSerializer(serializers.ModelSerializer):
    def validate(self, data):
        print(data)
        return data

    def create(self, validated_data):
        article = Article(**validated_data)
        print('val=', validated_data)
        article.save()
        return article

    def update(self, instance, validated_data):
        # instance에는 입력된 object가 담긴다.
        print(instance,"or", validated_data)
        instance.title = validated_data['title']
        instance.save()
        return instance

    class Meta:
        model = Article
        fields = ["user", "title", "category", "img_url"]