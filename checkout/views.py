from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
import os

from .forms import OrderForm
from bag.contexts import bag_contents

import stripe

# Get Stripe keys from environment variables
stripe_public_key = os.getenv('STRIPE_PUBLIC_KEY', '')
stripe_secret_key = os.getenv('STRIPE_SECRET_KEY', '')

def checkout(request):
    stripe.api_key = stripe_secret_key
    
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))
    
    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)
    
    order_form = OrderForm()
    
    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. Did you forget to set it in your environment?')
    
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': 'test_client_secret',
    }

    return render(request, template, context)