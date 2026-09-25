from django.db import models


class Payment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('payment_link_created', 'Payment Link Created'),
        ('awaiting_payment', 'Awaiting Payment'),
        ('paid', 'Paid'),
        ('failed', 'Failed'),
        ('cancelled', 'Cancelled'),
        ('refunded', 'Refunded'),
    ]

    customer = models.ForeignKey('customers.Customer', on_delete=models.PROTECT, related_name='payments')
    invoice_id = models.CharField(max_length=100, blank=True)
    reference = models.CharField(max_length=100, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default='USD')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')
    paypal_order_id = models.CharField(max_length=255, blank=True)
    paypal_capture_id = models.CharField(max_length=255, blank=True)
    transaction_id = models.CharField(max_length=255, blank=True)
    failure_reason = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Payment {self.id} - {self.customer.name} ({self.amount} {self.currency})"
