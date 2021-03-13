# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Snacks


class SnacksListView(ListView):
    template_name = "snacks_list.html"
    model = Snacks


class SnacksDetailView(DetailView):
    template_name = "snacks_detail.html"
    model = Snacks