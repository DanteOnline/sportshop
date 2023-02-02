from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView
from .models import Partner


class PartnerListView(LoginRequiredMixin, ListView):
    # template_name = 'sport_equipment/about.html'
    model = Partner