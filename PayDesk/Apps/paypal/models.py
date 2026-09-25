from django.db import models


class PayPalSettings(models.Model):
    ENVIRONMENT_CHOICES = [
        ('sandbox', 'Sandbox'),
        ('live', 'Live'),
    ]

    environment = models.CharField(max_length=20, choices=ENVIRONMENT_CHOICES, default='sandbox')
    client_id = models.CharField(max_length=255)
    client_secret = models.CharField(max_length=255)
    webhook_id = models.CharField(max_length=255, blank=True)
    currency = models.CharField(max_length=3, default='USD')
    business_name = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "PayPal Settings"
        verbose_name_plural = "PayPal Settings"

    def __str__(self):
        return f"PayPal Settings ({self.environment})"

    def get_masked_secret(self):
        if not self.client_secret:
            return ""
        return "*" * (len(self.client_secret) - 4) + self.client_secret[-4:]
