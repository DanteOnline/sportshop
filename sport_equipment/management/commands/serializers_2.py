from django.core.management.base import BaseCommand
from rest_framework import serializers
from .python_models import Category

# WORK WITHOUT DJANGO

class Command(BaseCommand):

    def handle(self, *args, **options):
        class CategorySerializer(serializers.Serializer):
            name = serializers.CharField(max_length=128)
            rating = serializers.IntegerField()

            def create(self, validated_data):
                return Category(**validated_data)

            def update(self, instance, validated_data):
                instance.name = validated_data.get('name', instance.name)
                instance.rating = validated_data.get('rating', instance.rating)
                return instance

        data = {'name': 'Плавание', 'rating': 3}
        serializer = CategorySerializer(data=data)
        serializer.is_valid()
        category = serializer.save()

        print(category)

        data = {'name': 'Плавание', 'rating': 4}
        serializer = CategorySerializer(category, data=data)
        serializer.is_valid()
        category = serializer.save()

        print(category)

        data = {'rating': 5}
        serializer = CategorySerializer(category, data=data, partial=True)
        serializer.is_valid()
        category = serializer.save()
        print(category)

        data = {'rating': 6}
        serializer = CategorySerializer(category, data=data)
        is_valid = serializer.is_valid()
        print(serializer.errors)
        print(is_valid)


