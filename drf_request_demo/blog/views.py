from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import ArticleSerializer
from .permissions import BlocklistPermissions,IsOwnerOrReadOnly
from .models import Article
from .pagination import (LargePageNumberPagination,LargeLimitOffsetPagination,PostCursorPagination,CustomPagination)

class ArticleList(generics.ListCreateAPIView):
    queryset=Article.objects.all()
    serializer_class=ArticleSerializer
    permission_classes=[BlocklistPermissions,IsAuthenticatedOrReadOnly]

    def perform_create(self,serializer):
        serializer.save(owner=self.request.user)


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Article.objects.all()
    serializer_class=ArticleSerializer
    permission_classes=[BlocklistPermissions,IsOwnerOrReadOnly]


# #Filter by current authenticated user
# class ArticleListByUser(generics.ListAPIView):
#     serializer_class=ArticleSerializer

#     def get_queryset(self):
#         return Article.objects.filter(owner=self.request.user)


# # filter using username from url


class PostListPage(generics.ListAPIView):
    queryset=Article.objects.all()
    serializer_class=ArticleSerializer
    
class PostListLargePage(generics.ListAPIView):
    queryset=Article.objects.all()
    serializer_class=ArticleSerializer
    pagination_class=LargePageNumberPagination
    
class PostListLimitOffset(generics.ListAPIView):
    queryset=Article.objects.all()
    serializer_class=ArticleSerializer
    pagination_class=LargeLimitOffsetPagination
    
class PostListCursor(generics.ListAPIView):
    queryset=Article.objects.all()
    serializer_class=ArticleSerializer
    pagination_class=PostCursorPagination

class PostListCustom(generics.ListAPIView):
    queryset=Article.objects.all()
    serializer_class=ArticleSerializer
    pagination_class=CustomPagination
    