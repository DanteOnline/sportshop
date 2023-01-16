from rest_framework import serializers
from django.core.management.base import BaseCommand
from sport_equipment.models import Category, CategoryCard, Tag, Equipment


class Command(BaseCommand):

    def handle(self, *args, **options):
        class CategorySerializer(serializers.ModelSerializer):
            class Meta:
                model = Category
                fields = '__all__'

        class CategoryCardSerializer(serializers.ModelSerializer):
            class Meta:
                model = CategoryCard
                fields = '__all__'
                # exclude = ['category']

        class TagSerializer(serializers.ModelSerializer):

            class Meta:
                model = Tag
                fields = ['name']

        class EquipmentSerializer(serializers.ModelSerializer):
            category = CategorySerializer()
            tags = serializers.StringRelatedField(many=True)
            #tags = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
            # tags = serializers.HyperlinkedRelatedField(
            #     many=True,
            #     read_only=True,
            #     view_name='sport_equipment:category-detail'
            # )
            # tags = TagSerializer(many=True)

            class Meta:
                model = Equipment
                fields = '__all__'

        Equipment.objects.all().delete()
        CategoryCard.objects.all().delete()
        Category.objects.all().delete()

        category = Category.objects.create(name='Плавание', rating=4)
        serializer = CategorySerializer(category)
        print(serializer.data)

        category_card = CategoryCard.objects.create(category=category, text='Текст карточки')
        serializer = CategoryCardSerializer(category_card)
        print(serializer.data)

        tags = []
        tag = Tag.objects.create(name='Атлетика')
        serializer = TagSerializer(tag)
        print(serializer.data)
        tags.append(tag)

        tag = Tag.objects.create(name='Красиво')
        serializer = TagSerializer(tag)
        print(serializer.data)
        tags.append(tag)

        equipment = Equipment.objects.create(name='Ласты', category=category)
        for tag in tags:
            equipment.tags.add(tag)
        equipment.save()

        serializer = EquipmentSerializer(equipment)
        print(serializer.data)
