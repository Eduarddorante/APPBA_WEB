from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
# class based views
from django.views.generic import View, TemplateView
from ...apps.utils.mixins import AdminRequiredMixin,UsuarioRequiredMixin
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
# login required
from django.contrib.auth.mixins import LoginRequiredMixin
# coordinador models
# Create your views here.

class ReportesTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'reportes/constancia.html'

class ReportesPageTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'reportes/Reportes.html'
