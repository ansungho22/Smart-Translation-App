from .models import User
from rest_framework import serializers, fields
from django.contrib.auth import *
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import update_last_login

User = get_user_model()


JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER


class UserCreateSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    nickname = serializers.CharField(required=True)
    language = serializers.CharField(required=True)

    def create(self, validated_data):
        user = User.objects.create(  # User 생성
            email=validated_data["email"],
            username=validated_data["username"],
            nickname=validated_data["nickname"],
            language=validated_data["language"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.nickname = validated_data.get("nickname", instance.nickname)
        instance.language = validated_data.get("language", instance.language)
        instance.set_password(validated_data["password"])
        instance.save()
        return instance


class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=64)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)
        user = authenticate(email=email, password=password)

        if user is None:
            return {"email": "None"}
        try:
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)  # 토큰 발행
            update_last_login(None, user)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                "User with given email and password does not exists"
            )
        return {"email": user.email, "token": jwt_token}
