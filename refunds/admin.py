from django.contrib import admin

from django.contrib import admin
from .models import RefundRequest

@admin.register(RefundRequest)
class RefundRequestAdmin(admin.ModelAdmin):
    pass

