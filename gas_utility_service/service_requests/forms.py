from django import forms
from .models import ServiceRequest, ServiceRequestType

class ServiceRequestForm(forms.ModelForm):
    """
    Form for customers to submit service requests
    """
    request_type = forms.ModelChoiceField(
        queryset=ServiceRequestType.objects.all(),
        help_text="Select the type of service request"
    )

    class Meta:
        model = ServiceRequest
        fields = ['request_type', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }