from django.shortcuts import render
from .serializers import SnippetSerializer
from rest_framework.authentication import SessionAuthentication,BasicAuthentication,TokenAuthentication
from .models import Snippet
from rest_framework import generics,permissions
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response


class SnippetList(generics.ListCreateAPIView):
    queryset=Snippet.objects.all()
    serializer_class=SnippetSerializer
    # authentication_classes=[SessionAuthentication,BasicAuthentication,TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]


    def perform_create(self,serializer):
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Snippet.objects.all()
    serializer_class=SnippetSerializer
    authentication_classes=[SessionAuthentication,BasicAuthentication,TokenAuthentication]
    permission_classes=[permissions.IsAuthenticatedOrReadOnly,permissions.IsAdminUser]

    def perform_update(self,serializer):
        if serializer.instance.owner!=self.request.user:
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied("you must be owner to update")
        serializer.save()

class PublicView(APIView):
    permission_classes=[AllowAny]

    def get(self,request):
        return Response({"message":"This method is for the unauthenticated users"})

class PrivateView(APIView):
    permission_classes=[IsAuthenticated]

    def get(self, request):
        return Response({"message":f"private endpoint for {request.user}. authenticated user"})