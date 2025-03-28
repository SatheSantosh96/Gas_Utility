from django.urls import path
from . import views

urlpatterns = [
    path('requests/', views.SupportRequestListView.as_view(), name='support_request_list'),
    path('requests/<int:pk>/update/', 
         views.UpdateServiceRequestStatusView.as_view(), 
         name='update_service_request_status'),
    path('requests/<int:pk>/notes/', 
         views.AddSupportNoteView.as_view(), 
         name='add_support_note'),
]