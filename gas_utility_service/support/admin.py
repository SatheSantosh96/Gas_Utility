from django.contrib import admin
from .models import SupportNote

@admin.register(SupportNote)
class SupportNoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'service_request', 'support_rep', 'created_at')
    list_filter = ('support_rep', 'created_at')
    search_fields = ('service_request__id', 'support_rep__username', 'note_text')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)
    fieldsets = (
        ('Service Request Information', {
            'fields': ('service_request',)
        }),
        ('Support Representative', {
            'fields': ('support_rep',)
        }),
        ('Note Details', {
            'fields': ('note_text', 'created_at')
        }),
    )
