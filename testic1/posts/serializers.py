from rest_framework import serializers
from .models import Category, Post, Comment
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    post = serializers.SlugRelatedField(slug_field='name', queryset=Post.objects.all())
    class Meta:
        model = Comment
        fields = ('id', 'author', 'text', 'post', 'data_create')


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    category = serializers.SlugRelatedField(slug_field='name', queryset=Category.objects.all())
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'author', 'name', 'full_text', 'category', 'data_create', 'data_update', 'likes_count',)

    def get_likes_count(self, obj):
        return obj.likes.count()


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name', 'description',)