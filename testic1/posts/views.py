from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import  Category, Post, Comment
from .serializers import  CategorySerializer, PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly



class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]


class PostViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['data_create', 'name',]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):

        post = self.get_object()
        post.likes.add(request.user)
        post.save()
        return Response({'status': 'пост лайкнут'})

    @action(detail=True, methods=['post'])
    def unlike(self, request, pk=None):

        post = self.get_object()
        post.likes.remove(request.user)
        post.save()
        return Response({'status': 'лайк с поста убран'})


class CommentViewSet(viewsets.ModelViewSet):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAdminOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


