from .models import *
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from PIL import Image
from .models import Profile


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            password=make_password(validated_data['password'])
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'id', 'email', 'is_staff', 'is_active']


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ProfileListSerializer(serializers.ModelSerializer):

    username = serializers.CharField(source='user.username')
    skin = serializers.ImageField(max_length=None)
    skin_thumb_url = serializers.SerializerMethodField('get_thumb_url')
    skin_url = serializers.SerializerMethodField('get_image_url')
    date_joined = serializers.CharField(source='user.date_joined')

    class Meta:
        model = Profile
        fields = ['username', 'id', 'user', 'skin', 'skin_thumb', 'skin_thumb_url', 'skin_url', 'subscription', 'is_media', 'date_joined']

    def get_image_url(self, obj):
        return self.context['request'].build_absolute_uri(obj.skin.url)

    def get_thumb_url(self, obj):
        skin_thumb_url = 'http://127.0.0.1:8000/media/' + obj.skin_thumb
        return skin_thumb_url


class ProfileUpdateSerializer(serializers.ModelSerializer):

    skin = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Profile
        fields = ['skin']


class ProfileDetailSerializer(serializers.ModelSerializer):

    username = serializers.CharField(source='user.username')
    skin_url = serializers.SerializerMethodField('get_image_url')
    skin_thumb_url = serializers.SerializerMethodField('get_thumb_url')

    class Meta:
        model = Profile
        fields = '__all__'

    def get_image_url(self, obj):
        return self.context['request'].build_absolute_uri(obj.skin.url)
    def get_thumb_url(self, obj):
        skin_thumb_url = 'http://127.0.0.1:8000/media/' + obj.skin_thumb
        return skin_thumb_url


