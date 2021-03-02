from celery import shared_task
import africastalking
from.models import Order
username = "sandbox"    # use 'sandbox' for development in the test environment
api_key = "4b687203c43211be0e43105531bf92d7d8ad44d778bdfcf869988c465049291e"
africastalking.initialize(username, api_key)
sms = africastalking.SMS

@shared_task
def send_sms(order_id):
    """
  
    Task to send an sms notification when an order is
    successfully created.
    """
    order = Order.objects.get(id=order_id)
   
    message = f'Dear {order.customer.user} You have successfully placed an order.Your order ID is {order.id}.'
    response=sms.send(message,["+254728826517"])
    return response
#    sudo service redis-server stop
# $ celery -A backend_challenge worker -l INFO



