from django.conf.urls.static import static
from django.urls import path, include
from sport_equipment import views
from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter
from . import views
from . import viewsets

app_name = 'drf_api'

router = DefaultRouter()
router.register(r'category', viewsets.CategoryViewSet, basename='category')
router.register(r'mixin', viewsets.CategoryMixinViewSet)

urlpatterns = [
    path('', views.ListCategoryAPIView.as_view(), name='list-category-api-view'),
    path('generic-list/', views.ListCategoryView.as_view(), name='list-category-view'),
    path('generic-create/', views.CreateCategoryView.as_view(), name='create-category-view'),
    path('generic-create-list/', views.ListCreateCategoryView.as_view(), name='list-create-category-view'),
    path('viewset/', include(router.urls)),
    path('filter-list/<str:name_part>/', views.FilterListView.as_view()),
]
