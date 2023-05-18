# import io
# from rest_framework.parsers import JSONParser
# from rest_framework.renderers import JSONRenderer
from rest_framework import serializers
from .models import User, Post


# class Model:
#     def __init__(self, name, email, password):
#         self.name = name
#         self.email = email
#         self.password = password


class UserSerializes(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email')

# class UserSerializes(serializers.Serializer):
#     name = serializers.CharField(max_length=200)
#     email = serializers.EmailField()
#     password = serializers.CharField(max_length=75)
#
#     def create(self, validated_data):
#         return User.objects.create(**validated_data)
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.email = validated_data.get('email', instance.email)
#         instance.password = validated_data.get('password', instance.password)
#         instance.save()
#
#         return instance


# def toJSON():
#     model = Model('Doniyor', 'ddonierov68@gmail.com', 'zxcasdqwe123D')
#     mode_sr = UserSerialize(model)
#     print(mode_sr.data)
#     json = JSONRenderer().render(mode_sr.data)
#     print(json)
#
#
# def decode():
#     stream = io.BytesIO(b'{"name":"Doniyor","email":"ddonierov68@gmail.com","password":"zxcasdqwe123D"}')
#     data = JSONParser().parse(stream)
#     serializer = UserSerializes(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)
