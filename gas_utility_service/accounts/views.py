from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import CustomerRegistrationForm
from .models import Customer
import random
import string
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.urls import reverse_lazy

class CustomerRegistrationView(CreateView):
    form_class = CustomerRegistrationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        # Generate a unique 10-digit account number
        account_number = ''.join(random.choices(string.digits, k=10))
        
        # Ensure the account number is unique
        while Customer.objects.filter(account_number=account_number).exists():
            account_number = ''.join(random.choices(string.digits, k=10))
        
        # Assign the generated account number to the instance before saving
        form.instance.account_number = account_number
        return super().form_valid(form)
    

class ProfileView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        if request.user.is_staff:
            return redirect(reverse_lazy('support_request_list'))  # Redirect staff users
        return redirect(reverse_lazy('service_request_list'))  # Redirect normal users