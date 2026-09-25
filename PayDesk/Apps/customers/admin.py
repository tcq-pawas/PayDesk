from django.contrib import admin
from Apps.customers.models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['customer_id', 'name', 'email', 'phone', 'payment_amount', 'currency', 'created_at']
    search_fields = ['customer_id', 'name', 'email', 'phone']
    list_filter = ['currency', 'created_at']
    readonly_fields = ['created_at', 'updated_at']
