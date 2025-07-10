from django.contrib import admin

from django.contrib import admin
from .models import RefundRequest

@admin.register(RefundRequest)
class RefundRequestAdmin(admin.ModelAdmin):
    list_filter = ('status', 'created_at', 'country')
    readonly_fields = ('created_at', 'updated_at')

