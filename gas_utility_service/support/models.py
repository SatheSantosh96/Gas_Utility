from django.db import models

# Create your models here.
from django.db import models
from service_requests.models import ServiceRequest
from django.conf import settings
from django.db import models

class SupportNote(models.Model):
    """
    Notes added by support representatives to service requests
    """
    service_request = models.ForeignKey(ServiceRequest, on_delete=models.CASCADE, related_name='notes')
    support_rep = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    note_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Note for Request {self.service_request.id}"