from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import serializers

from api.serializers import UserSerializer,ProductSerializer
from api.models import Product


# Create your views here.


class SignUpView(APIView):

    def post(sel,request,*args,**kwargs):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)

class ProductsView(viewsets.ModelViewSet):

    serializer_class=ProductSerializer
    queryset=Product.objects.all()

    def create(self, request, *args, **kwargs):
        raise serializers.ValidationError("permission denied")
    
    def update(self, request, *args, **kwargs):
        raise serializers.ValidationError("permission denied")
    
    def destroy(self, request, *args, **kwargs):
        raise serializers.ValidationError("permission denied")
    
    





























