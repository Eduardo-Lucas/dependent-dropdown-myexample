from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import BusinessLine, ProfitCenter, Project
from .forms import BusinessLineForm, ProfitCenterForm, ProjectForm


# WELCOME
def welcome(request):
    return render(request, 'tractebel/welcome.html', {})


# BEGIN - BUSINESS LINE
class BusinessLineListView(ListView):
    model = BusinessLine
    context_object_name = 'businesses'


class BusinessLineCreateView(CreateView):
    model = BusinessLine
    form_class = BusinessLineForm
    success_url = reverse_lazy('tractebel:businessline_list')


class BusinessLineUpdateView(UpdateView):
    model = BusinessLine
    form_class = BusinessLineForm
    success_url = reverse_lazy('tractebel:businessline_list')


class BusinessLineDeleteView(DeleteView):
    model = BusinessLine
    success_url = reverse_lazy('tractebel:businessline_list')
# END - BUSINESS LINE


# BEGIN - PROFIT CENTER
class ProfitCenterListView(ListView):
    model = ProfitCenter
    context_object_name = 'profits'


class ProfitCenterCreateView(CreateView):
    model = ProfitCenter
    form_class = ProfitCenterForm
    success_url = reverse_lazy('tractebel:profit_list')


class ProfitCenterUpdateView(UpdateView):
    model = ProfitCenter
    form_class = ProfitCenterForm
    success_url = reverse_lazy('tractebel:profit_list')


class ProfitCenterDeleteView(DeleteView):
    model = ProfitCenter
    success_url = reverse_lazy('tractebel:profit_list')
# END - PROFIT CENTER


# BEGIN - PROJECT
class ProjectListView(ListView):
    model = Project
    context_object_name = 'projects'


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy('tractebel:project_list')


class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy('tractebel:project_list')


class ProjectDeleteView(DeleteView):
    model = Project
    success_url = reverse_lazy('tractebel:project_list')


# END - PROJECT


def load_profit_center(request):
    business_id = request.GET.get('businessline')
    profits = ProfitCenter.objects.filter(businessline_id=business_id).order_by('description')
    return render(request, 'tractebel/profit_dropdown_list_options.html', {'profits': profits})
