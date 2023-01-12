from rest_framework.viewsets import ModelViewSet
from .serializers import CategorySerializer
from .models import Category


class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

