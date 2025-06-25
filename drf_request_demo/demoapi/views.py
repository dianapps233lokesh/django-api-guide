from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Item
from .serializers import ItemSerializer
import json

class ItemView(APIView):

    def get(self, request):
        search = request.query_params.get('search', '')
#     ✅ request.query_params.get('search', '')

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