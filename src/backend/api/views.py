from django.contrib.auth.models import User
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveDestroyAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from blog.models import Article
from .serializers import (
    ArticleSerializer,
    UserCreateSerializer,
    ArticleCreateSerializer,
    ArticleDeleteSerializer,
    ArticleDetailSerializer,
    UserSerializer,
)


# Create your views here.
class UserDetailView(RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


# class UserDeletelView(DestroyAPIView):
#     serializer_class = UserSerializer
#     permission_classes = [IsAuthenticated]

#     def get_object(self):
#         return self.request.user

#     def destroy(self, request, *args, **kwargs):
#         self.perform_destroy(self.get_object())
#         return Response(status=204)


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer


class ArticleListView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer


class ArticleDetailView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = "slug"


class ArticleCreate(CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleCreateSerializer


class ArticleUpdate(RetrieveUpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = "slug"


class ArticleDelete(RetrieveDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDeleteSerializer
    lookup_field = "slug"
