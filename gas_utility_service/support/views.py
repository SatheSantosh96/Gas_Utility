from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import ListView, UpdateView
from service_requests.models import ServiceRequest
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from service_requests.models import ServiceRequest
from .models import SupportNote

class SupportRequestListView(UserPassesTestMixin, ListView):
    """
    View for support representatives to list all service requests
    """
    model = ServiceRequest
    template_name = 'support/request_list.html'
    context_object_name = 'requests'

    def test_func(self):
        return self.request.user.is_staff

class UpdateServiceRequestStatusView(UserPassesTestMixin, UpdateView):
    """
    View for support representatives to update request status
    """
    model = ServiceRequest
    fields = ['status']
    template_name = 'support/update_request.html'
    success_url = reverse_lazy('support_request_list')

    def test_func(self):
        return self.request.user.is_staff
    
class AddSupportNoteView(UserPassesTestMixin, CreateView):
    model = SupportNote
    fields = ['note_text']
    template_name = 'support/add_note.html'

    def test_func(self):
        return self.request.user.is_staff

    def form_valid(self, form):
        form.instance.service_request_id = self.kwargs['pk']
        form.instance.support_rep = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('support_request_list')