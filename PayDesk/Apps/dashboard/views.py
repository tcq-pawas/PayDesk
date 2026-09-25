from django.shortcuts import render
from django.db import models
from Apps.customers.models import Customer
from Apps.payments.models import Payment


def index(request):
    total_customers = Customer.objects.count()
    total_amount_due = Customer.objects.aggregate(total=models.Sum('payment_amount'))['total'] or 0
    total_paid = Payment.objects.filter(status='paid').aggregate(total=models.Sum('amount'))['total'] or 0
    pending_payments = Payment.objects.filter(status='pending').count()
    failed_payments = Payment.objects.filter(status='failed').count()
    recent_payments = Payment.objects.select_related('customer').order_by('-created_at')[:10]

    context = {
        'total_customers': total_customers,
        'total_amount_due': total_amount_due,
        'total_paid': total_paid,
        'pending_payments': pending_payments,
        'failed_payments': failed_payments,
        'recent_payments': recent_payments,
    }
    return render(request, 'dashboard/index.html', context)
