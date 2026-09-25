from django.shortcuts import render
from Apps.payments.models import Payment


def list(request):
    payments = Payment.objects.select_related('customer').all()

    context = {
        'payments': payments,
    }
    return render(request, 'payments/list.html', context)
