from django.conf.urls.static import static
from django.urls import path, include
from sport_equipment import views
from django.conf import settings
from rest_framework.routers import DefaultRouter
from .api_views import CategoryModelViewSet

app_name = 'sport_equipment'

router = DefaultRouter()
router.register('categories', CategoryModelViewSet)

urlpatterns = [
    path('', views.equipment_list_view, name='main'),
    path('equipment-category/list/', views.CategoryListView.as_view(), name='equipment-category-list'),
    path('api/', include(router.urls)),
    path('about/', views.AboutTemplateView.as_view(), name='about'),

    path('category/detail/<int:pk>/', views.CategoryDetailView.as_view(), name='category-detail'),
    path('category/create/', views.CategoryCreateView.as_view(), name='category-create'),
    path('category/update/<int:pk>/', views.CategoryUpdateView.as_view(), name='category-update'),
    path('category/delete/<int:pk>/', views.CategoryDeleteView.as_view(), name='category-delete'),
    path('contacts/', views.ContactFormView.as_view(), name='contacts'),
    path('task-result/<str:task_id>/', views.TaskResultView.as_view(), name='task_result'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)