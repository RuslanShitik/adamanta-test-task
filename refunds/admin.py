from django.contrib import admin
from .models import RefundRequest
from import_export.resources import ModelResource
from import_export.admin import ExportMixin


class RefundRequestResource(ModelResource):
    class Meta:
        model = RefundRequest
        fields = (
            'user',
            'order_number',
            'order_date',
            'first_name',
            'last_name',
            'phone_number',
            'email',
            'country',
            'address',
            'postal_code',
            'city',
            'products',
            'reason',
            'bank_name',
            'account_type',
            'iban',
            'iban_verified',
            'created_at',
            'updated_at',
            'status',
        )
        export_order = fields


@admin.register(RefundRequest)
class RefundRequestAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = RefundRequestResource
    list_filter = ('status', 'created_at', 'country')
    readonly_fields = ('created_at', 'updated_at')
