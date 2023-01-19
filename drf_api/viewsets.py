from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action

from .filters import CategoryFilter
from .serializers import CategorySerializer
from rest_framework import viewsets
from rest_framework.response import Response
from sport_equipment.models import Category
from rest_framework import mixins

class CategoryViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving.
    """
    def list(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Category.objects.all()
        category = get_object_or_404(queryset, pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    # @action(detail=True, methods=['post'])
    @action(detail=False, methods=['post'])
    def get_first_category(self, request, pk=None):
        print('PK', pk)
        category = Category.objects.all().first()
        serializer = CategorySerializer(category)
        return Response(serializer.data)


class CategoryMixinViewSet(mixins.CreateModelMixin,
                                mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # filterset_fields = ['rating__lte', 'is_active']
    filterset_class = CategoryFilter