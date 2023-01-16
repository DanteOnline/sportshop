from rest_framework.viewsets import ModelViewSet
from rest_framework.renderers import AdminRenderer
from .serializers import CategorySerializer
from .models import Category


class CategoryModelViewSet(ModelViewSet):

    # renderer_classes = [AdminRenderer]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

