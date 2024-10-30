from rest_framework import viewsets, generics, permissions
from .models import Board, Post, ImagePost, Comment
from .serializers import BoardSerializer, PostSerializer, ImagePostSerializer, CommentSerializer
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.response import Response
from rest_framework import status


class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

@method_decorator(csrf_exempt, name='dispatch')
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user if self.request.user.is_authenticated else None)

    @method_decorator(csrf_exempt)  # CSRF 검사를 비활성화
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset(self):
        # 특정 게시판 ID로 필터링 가능
        board_id = self.request.query_params.get('board_id')
        if board_id:
            return Post.objects.filter(board_id=board_id)
        return Post.objects.all()

@method_decorator(csrf_exempt, name='dispatch')
class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        board_id = self.request.query_params.get('board_id')
        if board_id:
            return Post.objects.filter(board_id=board_id)
        return Post.objects.all()

    def perform_create(self, serializer):
        # 보드 객체를 가져오고, 현재 사용자로 작성자를 설정
        board = serializer.validated_data['board']
        serializer.save(author=self.request.user)

    def create(self, request, *args, **kwargs):
        # 요청의 데이터를 직렬화합니다.
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # 유효성 검사를 수행합니다.

        # perform_create 메서드를 호출하여 데이터베이스에 저장합니다.
        self.perform_create(serializer)

        # 성공적으로 생성된 경우, 응답을 반환합니다.
        return Response(serializer.data, status=status.HTTP_201_CREATED)


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
