from django.shortcuts import render
from .models import Equipment


def equipment_list_view(request):
    equipment_list = Equipment.objects.all()
    equipment_list_own = Equipment.objects.filter(is_own_shop=True)
    context = {
        'equipment_list': equipment_list,
        'equipment_list_own': equipment_list_own
    }
    return render(request, 'sport_equipment/equipment_list.html', context)