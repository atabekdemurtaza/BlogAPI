from rest_framework import serializers
from posts.models import Post
from django.contrib.auth import get_user_model

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'owner', 'title', 'body', 'created_at')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')
