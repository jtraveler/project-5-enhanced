from django.http import HttpResponse


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)
    
    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        
        # Retrieve the Charge to get billing details
        import stripe
        from django.conf import settings
        
        stripe.api_key = settings.STRIPE_SECRET_KEY
        
        # Get the charge ID from the intent
        charge_id = intent.get('latest_charge')
        
        if charge_id:
            # Retrieve the charge object which contains billing details
            charge = stripe.Charge.retrieve(charge_id)
            
            print("=" * 50)
            print("PAYMENT INTENT ID:", intent.get('id'))
            print("CHARGE ID:", charge_id)
            print("BILLING DETAILS:", charge.billing_details)
            print("METADATA:", intent.get("metadata"))
            print("SHIPPING:", intent.get("shipping"))
            print("=" * 50)
        
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
    
    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)