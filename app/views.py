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


        new = User.objects.create(
            name=req.data['name'],
            email=req.data['email'],
            password=req.data['password'],
        )
        return Response(UserSerializes(new).data)