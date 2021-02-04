from rest_framework import serializers
from .models import Order,Customer

class CustomerSerializer(serializers.ModelSerializer):
     class Meta:
        model = Customer
        fields = ("phone",)

class OrderSerializer(serializers.ModelSerializer):
    customer_phone = serializers.SerializerMethodField()
    send_sms=serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ("item", "amount","customer_phone","send_sms")

    def get_customer_phone(self, obj):
        return obj.customer.phone

    def get_send_sms(self, obj):
        message = f'Dear {obj.customer.user} You have successfully placed an order.Your order ID is {obj.id}.An SMS was sent confirming receipt of your order'
        return message
