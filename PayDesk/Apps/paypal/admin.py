from django.contrib import admin
from Apps.paypal.models import PayPalSettings


@admin.register(PayPalSettings)
class PayPalSettingsAdmin(admin.ModelAdmin):
    list_display = ['environment', 'business_name', 'currency', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj:
            if 'client_secret' in form.base_fields:
                form.base_fields['client_secret'].widget.attrs['readonly'] = True
                form.base_fields['client_secret'].help_text = "For security, the client secret cannot be edited here."
        return form
