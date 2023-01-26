from rest_framework.serializers import ModelSerializer
from .models import MyUser


class BaseUserSerializer(ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('username', 'email', 'password', 'is_staff')


class ShortUserSerializer(ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('username', 'email')