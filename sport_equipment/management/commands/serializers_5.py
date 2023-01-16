from rest_framework import serializers
from django.core.management.base import BaseCommand
from .python_models import Category, CategoryCard, Equipment, Tag

# WORK WITHOUT DJANGO
class Command(BaseCommand):

    def handle(self, *args, **options):
        class CategorySerializer(serializers.Serializer):
            name = serializers.CharField(max_length=128)
            rating = serializers.IntegerField()

        class CategoryCardSerializer(serializers.Serializer):
            text = serializers.CharField(max_length=1024)
            category = CategorySerializer()

        class TagSerializer(serializers.Serializer):
            name = serializers.CharField(max_length=32)

        class EquipmentSerializer(serializers.Serializer):
            name = serializers.CharField(max_length=128)
            category = CategorySerializer()
            tags = TagSerializer(many=True)

        category = Category('Плавание', 4)
        serializer = CategorySerializer(category)
        print(serializer.data)
        print(type(serializer.data))

        category_card = CategoryCard(category, 'Текст карточки')
        serializer = CategoryCardSerializer(category_card)
        print(serializer.data)

        tags = []
        tag = Tag(name='Атлетика')
        serializer = TagSerializer(tag)
        print(serializer.data)
        tags.append(tag)

        tag = Tag(name='Красиво')
        serializer = TagSerializer(tag)
        print(serializer.data)
        tags.append(tag)

        equipment = Equipment('Ласты', category, tags)
        serializer = EquipmentSerializer(equipment)
        print(serializer.data)
