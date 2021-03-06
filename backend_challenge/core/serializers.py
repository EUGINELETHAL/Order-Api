from rest_framework import serializers
from .models import Order, Customer
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError


class CustomerSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Customer
        fields = ("phone", "code")
    

    

class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ("item", "amount","customer")
    def validate(self, data):
        if data.get('customer') is None:
            raise serializers.ValidationError(
                    'Please Update your profile details'
                )

        return data

  
    def create(self, validated_data):
        request = self.context.get('request', None)
        if request is None:
            return False
        
        customer=request.user.customer
        print(customer)
        '''Create a new Customer instance, given the accepted data.'''
        return Order.objects.create(**validated_data,customer=customer)
