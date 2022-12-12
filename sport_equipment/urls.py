from django.urls import path
from .views import equipment_list_view

app_name = 'sport_equipment'

urlpatterns = [
    path("", equipment_list_view, name='equipment_list'),
]