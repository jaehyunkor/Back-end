# views.py
from rest_framework import viewsets, permissions
from .models import Board, Post, ImagePost, Comment
from .serializers import BoardSerializer, PostSerializer, ImagePostSerializer, CommentSerializer
from django.views.generic import ListView

class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        board_id = self.request.query_params.get('board_id')
        if board_id:
            return Post.objects.filter(board_id=board_id)
        return Post.objects.all()

    def perform_create(self, serializer):
        board = serializer.validated_data['board']
        serializer.save(author=self.request.user)

class ImagePostViewSet(viewsets.ModelViewSet):
    queryset = ImagePost.objects.all()
    serializer_class = ImagePostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        board = serializer.validated_data['board']
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        post_id = self.request.query_params.get('post_id')
        if post_id:
            return Comment.objects.filter(post_id=post_id)
        return Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class ImagePostListView(ListView):
    model = ImagePost
    template_name = 'image_post_list.html'  # 템플릿 파일 이름
    context_object_name = 'image_posts'
