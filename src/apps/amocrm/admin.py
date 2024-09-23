from django.contrib import admin
from .models import ClientData

@admin.register(ClientData)
class ClientDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'service', 'platform', 'created_at')
    list_filter = ('service', 'platform')
    search_fields = ('name', 'phone')
    readonly_fields = ('created_at',)

    def formatted_created_at(self, obj):
        return obj.get_created_at()
    formatted_created_at.short_description = 'Created At'
