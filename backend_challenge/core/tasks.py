import africastalking
from celery import shared_task
from django.conf import settings

from .models import Order

username = "sandbox"  # use 'sandbox' for development in the test environment
api_key = settings.AFRICASTALKING_API_KEY
africastalking.initialize(username, api_key)
sms = africastalking.SMS


@shared_task
def send_sms(order_id):
    """

    Task to send an sms notification when an order is
    successfully created.
    """
    order = Order.objects.select_related("customer").get(id=order_id)


    message = f"Dear {order.customer} You have successfully placed an order.Your order ID is {order.id}."
    response = sms.send(message, [order.customer.phone])
    return response


#    sudo service redis-server stop
# $ celery -A backend_challenge worker -l INFO
