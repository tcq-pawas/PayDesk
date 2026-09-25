from django.db import models


class Customer(models.Model):
    customer_id = models.CharField(max_length=100, unique=True, db_index=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=50, blank=True)
    address = models.TextField(blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    zip_code = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=100, blank=True)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default='USD')
    invoice_id = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} ({self.customer_id})"

    @property
    def payment_status(self):
        if hasattr(self, '_payment_status_cache'):
            return self._payment_status_cache
        try:
            latest_payment = self.payments.order_by('-created_at').first()
            if latest_payment:
                self._payment_status_cache = latest_payment.get_status_display()
            else:
                self._payment_status_cache = "No payments"
        except:
            self._payment_status_cache = "No payments"
        return self._payment_status_cache
