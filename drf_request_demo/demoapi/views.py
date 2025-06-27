from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,authentication,permissions
from .models import Item
from .serializers import ItemSerializer
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
class ItemView(APIView):

    def get(self, request):
        search = request.query_params.get('search', '')
#     request.query_params.get('search', '')

# .query_params accesses URL parameters (?search=value) from any request method.

# If absent, defaults to '' (empty string).
        # GET /api/items/?search=Pen

        print(search)
        items = Item.objects.filter(name__icontains=search)
        print(items)
        serializer = ItemSerializer(items, many=True, context={'request': request})
        print(serializer)
        return Response(serializer.data)

    def post(self, request):
        print("Raw Body:", request.body)
        print("Parsed Data:", request.data)
        print("Parsed Data:", type(request.data))
        serializer = ItemSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#         Raw Body: b'{"name":"Phone","description":"Smartphone"}'
# Parsed Data: {'name': 'Phone', 'description': 'Smartphone'}
# Parsed Data: <class 'dict'>



@api_view(['GET','POST'])
def greet(request):
    if request.method=='GET':
        return Response({"message":"hello world"},status=status.HTTP_200_OK)
    elif request.method=='POST':
        name=request.data.get('name')
        if not name:
            return Response({"error":"missing 'name' field"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message":f"Hello, name is {name}"},status=status.HTTP_201_CREATED)



class ListUsers(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAdminUser]

    def get(self,request,format=None):
        '''
        returns list of users
        '''
        usernames=[user.names for user in User.objects.all()]
        return Response(usernames)
    
@api_view(['GET','POST'])
def hello_word(request):
    if request.method == 'POST':
        return Response({"message":"Got some data!","data":request.data})
    return Response({"message":"I am lakku bhai"})