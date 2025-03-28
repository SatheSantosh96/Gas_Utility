from django.contrib import admin
from django.utils.html import format_html
from .models import ServiceRequestType, ServiceRequest

@admin.register(ServiceRequestType)
class ServiceRequestTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'request_type', 'status_display', 'created_at', 'updated_at', 'resolved_at')
    list_filter = ('status', 'request_type', 'created_at')
    search_fields = ('customer__username', 'request_type__name', 'description')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at', 'resolved_at')

    fieldsets = (
        ('Customer Information', {
            'fields': ('customer',)
        }),
        ('Request Details', {
            'fields': ('request_type', 'description', 'status', 'attachment')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at', 'resolved_at')
        }),
    )

    # ✅ Show colored status in the admin list display
    def status_display(self, obj):
        color = {
            "pending": "orange",
            "in_progress": "blue",
            "resolved": "green",
            "closed": "gray"
        }.get(obj.status, "black")
        return format_html('<span style="color: {};">{}</span>', color, obj.get_status_display())
    
    status_display.admin_order_field = 'status'
    status_display.short_description = 'Status'

    # ✅ Custom admin actions for bulk status update
    def mark_as_in_progress(self, request, queryset):
        queryset.update(status='in_progress')
    mark_as_in_progress.short_description = "Mark selected requests as In Progress"

    def mark_as_resolved(self, request, queryset):
        queryset.update(status='resolved')
    mark_as_resolved.short_description = "Mark selected requests as Resolved"

    def mark_as_closed(self, request, queryset):
        queryset.update(status='closed')
    mark_as_closed.short_description = "Mark selected requests as Closed"

    actions = [mark_as_in_progress, mark_as_resolved, mark_as_closed]