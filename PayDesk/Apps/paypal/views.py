from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from Apps.paypal.models import PayPalSettings


@csrf_protect
def settings(request):
    settings_obj = PayPalSettings.objects.first()

    if request.method == 'POST':
        if settings_obj:
            settings_obj.environment = request.POST.get('environment', 'sandbox')
            settings_obj.client_id = request.POST.get('client_id', '')
            settings_obj.client_secret = request.POST.get('client_secret', '')
            settings_obj.webhook_id = request.POST.get('webhook_id', '')
            settings_obj.currency = request.POST.get('currency', 'USD')
            settings_obj.business_name = request.POST.get('business_name', '')
            settings_obj.save()
        else:
            PayPalSettings.objects.create(
                environment=request.POST.get('environment', 'sandbox'),
                client_id=request.POST.get('client_id', ''),
                client_secret=request.POST.get('client_secret', ''),
                webhook_id=request.POST.get('webhook_id', ''),
                currency=request.POST.get('currency', 'USD'),
                business_name=request.POST.get('business_name', ''),
            )
        messages.success(request, 'PayPal settings updated successfully.')
        return redirect('paypal:settings')

    context = {
        'settings': settings_obj,
    }
    return render(request, 'paypal/settings.html', context)
