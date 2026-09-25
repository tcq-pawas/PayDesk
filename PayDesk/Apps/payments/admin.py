from django.contrib import admin
from Apps.payments.models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'amount', 'currency', 'status', 'invoice_id', 'created_at', 'completed_at']
    search_fields = ['invoice_id', 'reference', 'paypal_order_id', 'transaction_id', 'customer__name', 'customer__email']
    list_filter = ['status', 'currency', 'created_at']
    readonly_fields = ['created_at', 'updated_at', 'completed_at']
