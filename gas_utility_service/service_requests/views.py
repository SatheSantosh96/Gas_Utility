from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, DetailView
from django.urls import reverse_lazy
from .models import ServiceRequest
from .forms import ServiceRequestForm

class CreateServiceRequestView(LoginRequiredMixin, CreateView):
    """
    View to create a new service request
    """
    model = ServiceRequest
    form_class = ServiceRequestForm
    template_name = 'service_requests/create_request.html'
    success_url = reverse_lazy('service_request_list')

    def form_valid(self, form):
        form.instance.customer = self.request.user
        return super().form_valid(form)

class ServiceRequestListView(LoginRequiredMixin, ListView):
    """
    View to list service requests for a customer
    """
    model = ServiceRequest
    template_name = 'service_requests/request_list.html'
    context_object_name = 'requests'

    def get_queryset(self):
        return ServiceRequest.objects.filter(customer=self.request.user)

class ServiceRequestDetailView(LoginRequiredMixin, DetailView):
    """
    View to show details of a specific service request
    """
    model = ServiceRequest
    template_name = 'service_requests/request_detail.html'
