from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect

# models
from payment.models import BillingAddress
from payment.forms import BillingAddressForm,PaymentMethodForm
from order.models import Cart, Order

from django.conf import settings
import json
# view
from django.views.generic import TemplateView

from decimal import Decimal

from django.views.decorators.csrf import csrf_exempt


class CheckoutTemplateView(TemplateView):
    def get(self, request, *args, **kwargs):
        saved_address = BillingAddress.objects.get_or_create(user=request.user or None)
        saved_address = saved_address[0]
        form = BillingAddressForm(instance=saved_address)
        payment_method = PaymentMethodForm()
        order_qs = Order.objects.filter(user=request.user, ordered=False)
        order_item = order_qs[0].orderitems.all()
        order_total = order_qs[0].get_totals()

        context = {
            'billing_address': form,
            'order_item': order_item,
            'order_total': order_total,
            'payment_method': payment_method,

        }
        return render(request, 'store/checkout.html', context)

    def post(self, request, *args, **kwargs):
        pass