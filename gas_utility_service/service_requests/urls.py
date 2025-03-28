from django.urls import path
from . import views

urlpatterns = [
    path('', views.ServiceRequestListView.as_view(), name='service_request_list'),
    path('create/', views.CreateServiceRequestView.as_view(), name='create_service_request'),
    path('<int:pk>/', views.ServiceRequestDetailView.as_view(), name='service_request_detail'),
]