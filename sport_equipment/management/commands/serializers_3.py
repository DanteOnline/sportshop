from rest_framework import serializers
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        class CategorySerializer(serializers.Serializer):
            name = serializers.CharField(max_length=128)
            rating = serializers.IntegerField()

        data = {'name': 'Плавание', 'rating': 3}
        serializer = CategorySerializer(data=data)
        print(serializer.is_valid())  # True

        data = {'name': 'Плавание', 'rating': 'abc'}
        serializer = CategorySerializer(data=data)
        print(serializer.is_valid())  # False

        print(serializer.errors)  # {'rating': [ErrorDetail(string='A valid integer is required.', code='invalid')]}

        serializer.is_valid(raise_exception=True)
