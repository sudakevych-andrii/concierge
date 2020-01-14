from django.contrib.admin import ModelAdmin, register

from .models import Tenant, Room, Journal


@register(Tenant)
class TenantAdmin(ModelAdmin):
    list_display = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')


@register(Room)
class RoomAdmin(ModelAdmin):
    list_display = ('number', 'max_tenants')
    search_fields = ('number', 'max_tenants')
    readonly_fields = ['tenant', 'is_free']


@register(Journal)
class JournalAdmin(ModelAdmin):
    list_display = ('room', 'tenant', 'tenants_count', 'check_in_date', 'check_out_date')
    search_fields = ('room', 'tenant', 'tenants_count', 'check_in_date', 'check_out_date')
