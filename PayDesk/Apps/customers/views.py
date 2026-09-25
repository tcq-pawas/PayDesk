from django.shortcuts import render, get_object_or_404
from Apps.customers.models import Customer


def list(request):
    search_query = request.GET.get('search', '')
    customers = Customer.objects.all()

    if search_query:
        customers = customers.filter(
            name__icontains=search_query
        ) | customers.filter(
            email__icontains=search_query
        ) | customers.filter(
            customer_id__icontains=search_query
        )

    context = {
        'customers': customers,
        'search_query': search_query,
    }
    return render(request, 'customers/list.html', context)


def detail(request, id):
    customer = get_object_or_404(Customer, id=id)
    payments = customer.payments.all()

    context = {
        'customer': customer,
        'payments': payments,
    }
    return render(request, 'customers/detail.html', context)
