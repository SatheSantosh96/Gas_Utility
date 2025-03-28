from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings

class ServiceRequestType(models.Model):
    """
    Predefined service request types
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class ServiceRequest(models.Model):
    """
    Service request model to track customer requests
    """
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed')
    ]

    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    request_type = models.ForeignKey(ServiceRequestType, on_delete=models.PROTECT)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    
    

    def __str__(self):
        return f"{self.customer.username} - {self.request_type.name}"