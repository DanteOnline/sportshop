from rest_framework import serializers
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):

        class CategorySerializer(serializers.Serializer):
            name = serializers.CharField(max_length=128)
            rating = serializers.IntegerField()

            def validate_rating(self, value):
                if value < 0:
                    raise serializers.ValidationError('Рейтинг не может быть отрицательным')
                return value

            def validate(self, attrs):
                if attrs['name'] == 'Плавание' and attrs['rating'] <= 3:
                    raise serializers.ValidationError('У плавания не может быть такой низкий рейтинг')
                return attrs

        data = {'name': 'Зимний', 'rating': 3}
        serializer = CategorySerializer(data=data)
        print(serializer.is_valid())

        data = {'name': 'Зимний', 'rating': -10}
        serializer = CategorySerializer(data=data)
        print(serializer.is_valid())

        print(serializer.errors)

        data = {'name': 'Плавание', 'rating': 3}
        serializer = CategorySerializer(data=data)
        print(serializer.is_valid())
        print(serializer.errors)
