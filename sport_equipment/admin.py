from django.contrib import admin
from .models import Category, Equipment, Product, Excursion, DebugEquipment
import time
import django_rq
from .tasts import get_report_job



@admin.action(description='Get report')
def get_report(modeladmin, request, queryset):
    queue = django_rq.get_queue()
    job = queue.enqueue(get_report_job)
    print(job.id)
    print('Run task')


class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'create', 'update')

    actions = [get_report]


admin.site.register(Category, CategoryModelAdmin)
admin.site.register(Equipment)
admin.site.register(Excursion)
admin.site.register(Product)
admin.site.register(DebugEquipment)

# DebugEquipment.objects.all().first().buy()
