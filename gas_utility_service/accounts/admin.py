from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Customer  # Ensure Customer is correctly imported

admin.site.register(Customer)  # Register your model here
