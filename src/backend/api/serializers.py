from django.contrib.auth.models import User
from rest_framework import serializers as rest_serializers
from blog.models import Article


class ArticleSerializer(rest_serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"


class ArticleDetailSerializer(rest_serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ["title", "slug", "thumb", "author", "status"]


class ArticleCreateSerializer(rest_serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ["title", "thumb", "content", "author", "status"]

    def create(self, validated_data):
        validated_data["slug"] = validated_data["title"].lower().replace(" ", "-")
        return super().create(validated_data)


class ArticleDeleteSerializer(rest_serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"


class UserSerializer(rest_serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserCreateSerializer(rest_serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["username", "password"]

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user

    def update(self, instance, validated_data):
        validated_data["password"] = instance.password
        return super().update(instance, validated_data)
