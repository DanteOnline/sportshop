from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .models import Category


class CategorySerializer(ModelSerializer):
# class CategorySerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

