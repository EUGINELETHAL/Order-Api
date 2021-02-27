from rest_framework import serializers
from .models import Order, Customer


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ("phone", "code","user")
        read_only_fields = ['user']

    def create(self, validated_data):
        user = self.context.get('user', None)
        print(user.email)
        new_customer= Customer.objects.create(**validated_data,user=user)
        print(new_customer)
        '''Create a new Customer instance, given the accepted data.'''
        return new_customer

class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    customer_phone = serializers.SerializerMethodField()
    send_sms=serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ("item", "amount","customer_phone","send_sms","customer")

    def get_customer_phone(self, obj):
        return obj.customer.phone

    def get_send_sms(self, obj):
        message = f'Dear {obj.customer.user} You have successfully placed an order.Your order ID is {obj.id}.An SMS was sent confirming receipt of your order'
        return message
    def create(self, validated_data):
        request = self.context.get('request', None)
        if request is None:
            return False
        customer=request.user.customer
        print(customer)
        '''Create a new Customer instance, given the accepted data.'''
        return Order.objects.create(**validated_data,customer=customer)