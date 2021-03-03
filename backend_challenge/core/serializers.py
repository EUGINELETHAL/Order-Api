from rest_framework import serializers
from .models import Order, Customer
from django.contrib.auth.models import User



class CustomerSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Customer
        fields = ("phone", "code")
    

    

class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ("item", "amount","customer")


  
    def create(self, validated_data):
        request = self.context.get('request', None)
        if request is None:
            return False
        customer=request.user.customer
        print(customer)
        '''Create a new Customer instance, given the accepted data.'''
        return Order.objects.create(**validated_data,customer=customer)
