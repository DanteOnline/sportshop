from django.conf.urls.static import static
from django.urls import path, re_path
from sport_equipment import views
from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter
from . import api_views

app_name = 'user'

urlpatterns = [
    path('', api_views.UserListAPIView.as_view(), name='list-users'),
    re_path(
        r'^(?P<version>(v1.0|v2.0))/user/$',
        api_views.UserListAPIView.as_view(),
        name='list-users-version'
    ),

]
