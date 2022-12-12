from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Equipment, Category
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

def equipment_list_view(request):
    equipment_list = Equipment.objects.all()
    equipment_list_own = Equipment.objects.filter(is_own_shop=True)
    context = {
        'equipment_list': equipment_list,
        'equipment_list_own': equipment_list_own,
    }
    return render(request, 'sport_equipment/equipment_list.html', context)


# MVT - url
# def about_view(request):
#     return render(request, 'sport_equipment/about.html')

class AboutTemplateView(TemplateView):
    template_name = 'sport_equipment/about.html'


# CRUD - Category
class CategoryListView(ListView):
    model = Category
    template_name = 'sport_equipment/categories.html'
    context_object_name = 'categories'

    def get_queryset(self):
        # 1. Выборка
        return Category.objects.filter(is_active=True)

    def get_context_data(self, *args, **kwargs):
        # 4.
        context = super().get_context_data(*args, **kwargs)
        context['useful_information'] = 'ЧТо то полезное'
        return context

    def get(self, request, *args, **kwargs):
        # 5. Гет запрос
        print('request', request)
        return super().get(request, *args, **kwargs)

class CategoryDetailView(DetailView):
    model = Category

    # def get_queryset(self):
    # 2.
    #     pass
    #
    # def get_object(self, queryset=None):
    # 3.
    #     pass


class CategoryCreateView(CreateView):
    model = Category
    fields = ('name',)
    success_url = reverse_lazy('sport_equipment:category-list')

    # def form_valid(self, form):
    #     # 7. Валидация формы
    #     pass
    #
    # def form_invalid(self, form):
    #     pass
    def post(self, request, *args, **kwargs):
        # 6. Post запрос
        print('request', request)
        return super().post(request, *args, **kwargs)


class CategoryUpdateView(UpdateView):
    model = Category
    fields = ('name',)
    success_url = reverse_lazy('sport_equipment:category-list')

    # def get_success_url(self):
    #     pass


class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('sport_equipment:category-list')