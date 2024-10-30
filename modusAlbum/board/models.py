# models.py
from django.db import models
from django.contrib.auth.models import User

class Board(models.Model):
    TEXT = 'text'
    IMAGE = 'image'
    BOARD_TYPE_CHOICES = [
        (TEXT, 'Text Only'),
        (IMAGE, 'Image Only'),
    ]
    name = models.CharField(max_length=100, unique=True)  # 게시판 이름으로 구분
    description = models.TextField()
    board_type = models.CharField(max_length=10, choices=BOARD_TYPE_CHOICES, default=TEXT)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    #author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    board = models.ForeignKey(Board, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ImagePost(models.Model):
    image = models.ImageField(upload_to='images/')
    content = models.TextField()
    author = models.ForeignKey(User, related_name='image_posts', on_delete=models.CASCADE)
    board = models.ForeignKey(Board, related_name='image_posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image.url

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"
