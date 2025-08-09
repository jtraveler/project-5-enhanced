from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'subject',
        'name',
        'email',
        'created_at',
        'replied',
    )
    list_filter = (
        'replied',
        'created_at',
    )
    search_fields = (
        'name',
        'email',
        'subject',
        'message',
    )
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)
    
    # Add action to mark as replied
    actions = ['mark_as_replied']
    
    def mark_as_replied(self, request, queryset):
        queryset.update(replied=True)
    mark_as_replied.short_description = "Mark selected messages as replied"


admin.site.register(Contact, ContactAdmin)