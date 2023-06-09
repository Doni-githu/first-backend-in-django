from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User, Post
from .serialiazers import UserSerializes
from django.forms import model_to_dict

# Create your views here.


class UserAPIView(APIView):
    def get(self, req):
        users = User.objects.all()
        return Response(UserSerializes(users, many=True).data)

    def post(self, req):
        ser = UserSerializes(data=req.data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response({'user': ser.data})
    def put(self, req, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method PUT allowed'})
        try:
            instance = User.objects.get(pk=pk)
        except:
            return Response({'error': 'Method PUT not allowed'})

        serializer = UserSerializes(data=req.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'user': serializer.data})
    def delete(self, req, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method DELETE allowed'})

        return Response({'user': 'deleted ' + str(pk)})