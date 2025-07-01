from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Author,Book
from .serializers import AuthorSerializer,BookSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer
    
class BookViewSet(viewsets.ModelViewSet):
    queryset=Book.objects.all()
    serializer_class=BookSerializer

    @action(detail=True,methods='post')
    def publish(self, request, pk=None):
        return Response({
            'status':f'Book {pk} published'
        })