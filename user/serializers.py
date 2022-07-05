from rest_framework import serializers
from user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        # serializer model, field 지정
        model = User
        # 모든 필드를 사용하고 싶을 경우 fields = "__all__"로 사용
        # fields = "__all__"
        fields = ["id", "username"]


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "password",
            "email",
            "fullname",
            "join_date",
        ]

    username = serializers.CharField(required=True, min_length=4)
    email = serializers.EmailField(required=True)
    fullname = serializers.CharField(required=True)
    password = serializers.CharField(required=True, min_length=8)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            fullname=validated_data['fullname'],
        )
        user.set_password(validated_data['password'])

        user.save()
        return user
