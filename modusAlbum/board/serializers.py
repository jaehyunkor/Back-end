# serializers.py
from rest_framework import serializers
from .models import Board, Post, ImagePost, Comment

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['id', 'name', 'description', 'board_type']

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    board = serializers.PrimaryKeyRelatedField(queryset=Board.objects.all())

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'board', 'created_at']
        read_only_fields = ['author', 'created_at']

class ImagePostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    board = serializers.PrimaryKeyRelatedField(queryset=Board.objects.all())

    class Meta:
        model = ImagePost
        fields = ['id', 'image', 'content', 'board', 'created_at']

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at']
