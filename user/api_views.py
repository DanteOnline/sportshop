from rest_framework.generics import ListAPIView
from .serializers import BaseUserSerializer, ShortUserSerializer
from .models import MyUser


class UserListAPIView(ListAPIView):
    queryset = MyUser.objects.all()

    def get_serializer_class(self):
        print('VERSION', self.request.version)
        if self.request.version == 'v1.0':
            return BaseUserSerializer
        return ShortUserSerializer