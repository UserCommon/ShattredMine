from rest_framework import serializers
from .models import *
import datetime


class PostSerializer(serializers.ModelSerializer):
    preview = serializers.ImageField(max_length=None, allow_null=True)


    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'body', 'preview', 'tags', 'date_pub', 'author']


class PostCreateSerializer(serializers.ModelSerializer):
    author = serializers.RelatedField(source='profile.user.username', read_only=True)

    class Meta:
        model = Post
        fields = ['title', 'slug', 'body', 'preview', 'tags', 'author']




class PostUpdateSerializer(serializers.ModelSerializer):
    preview = serializers.ImageField(max_length=None, allow_null=True)
    
    class Meta:
        model = Post
        fields = ['title', 'body', 'preview', 'tags']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['title', 'slug']

