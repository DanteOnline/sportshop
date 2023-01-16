from rest_framework import serializers
from .models import Category


# class CategorySerializer(ModelSerializer):
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="sport_equipment:category-detail")
    class Meta:
        model = Category
        fields = '__all__'

