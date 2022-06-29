from rest_framework import serializers
from user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        # serializer model, field 지정
        model = User
        # 모든 필드를 사용하고 싶을 경우 fields = "__all__"로 사용
        # fields = "__all__"
        fields = ["id"]  # 부여되는 아이디만
