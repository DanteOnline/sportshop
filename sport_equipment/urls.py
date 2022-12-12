from django.urls import path
from sport_equipment import views

app_name = 'sport_equipment'

urlpatterns = [
    path('', views.equipment_list_view, name='main'),
    path('about/', views.AboutTemplateView.as_view(), name='about'),
    path('category/list/', views.CategoryListView.as_view(), name='category-list'),
    path('category/detail/<int:pk>/', views.CategoryDetailView.as_view(), name='category-detail'),
    path('category/create/', views.CategoryCreateView.as_view(), name='category-create'),
    path('category/update/<int:pk>/', views.CategoryUpdateView.as_view(), name='category-update'),
    path('category/delete/<int:pk>/', views.CategoryDeleteView.as_view(), name='category-delete'),
]