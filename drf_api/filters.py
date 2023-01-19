from rest_framework import generics
from django_filters import rest_framework as filters
from sport_equipment.models import Category


class CategoryFilter(filters.FilterSet):
    rating = filters.NumberFilter(field_name="rating", lookup_expr='lte')

    class Meta:
        model = Category
        fields = ['rating', 'is_active']