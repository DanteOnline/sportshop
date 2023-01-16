from django.core.management.base import BaseCommand
from .python_models import Category
import io


class Command(BaseCommand):

    def handle(self, *args, **options):
        from rest_framework import serializers

        class CategorySerializer(serializers.Serializer):
            name = serializers.CharField(max_length=128)
            rating = serializers.IntegerField()

        # 1. Сериализация в python объект
        category = Category('Плавание', 2)
        serializer = CategorySerializer(category)
        print(serializer.data)
        print(type(serializer.data))  # <class 'rest_framework.utils.serializer_helpers.ReturnDict'>

        from rest_framework.renderers import JSONRenderer
        renderer = JSONRenderer()
        json_bytes = renderer.render(serializer.data)
        print(json_bytes)
        print(type(json_bytes))  # <class 'bytes'>

        from rest_framework.parsers import JSONParser
        stream = io.BytesIO(json_bytes)
        data = JSONParser().parse(stream)
        print(data)
        print(type(data))  # <class 'dict'>

        serializer = CategorySerializer(data=data)
        print(serializer.is_valid())  # True
        print(serializer.validated_data)
        print(type(serializer.validated_data))  # <class 'collections.OrderedDict'>
