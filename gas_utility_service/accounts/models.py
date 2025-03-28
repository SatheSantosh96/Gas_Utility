from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class Customer(AbstractUser):
    """
    Extended user model for gas utility customers
    """
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    account_number = models.CharField(max_length=20, unique=True)