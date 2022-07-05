from rest_framework import serializers
from .models import Category, Article, Comment


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["name"]


class ArticleSerializer(serializers.ModelSerializer):
    def validate(self, data):
        return data

    def create(self, validated_data):
        article = Article(**validated_data)
        article.save()
        return article

    def update(self, instance, validated_data):
        print(validated_data)
        instance.title = validated_data['title']
        print(instance.title)
        instance.save()
        return instance

    class Meta:
        model = Article
        # fields = ["user","title","category","img_url"]
        fields = ["id","user","title","category","img_url"]

class CommentSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField(read_only=True)

    def get_username(self,obj):
        return obj.user.username
    class Meta:
        model = Comment
        fields = ["id","article","user","username","content","created_at","updated_at"]