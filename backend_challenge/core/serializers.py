from rest_framework import serializers
from .models import Order, Customer
from django.contrib.auth.models import User



class CustomerSerializer(serializers.ModelSerializer):
    user=serializers.PrimaryKeyRelatedField(read_only=True,source='user.email')
    class Meta:
        model = Customer
        fields = ("phone", "code","user")
    

    def create(self, validated_data):
        user = self.context.get('user', None)
        print(user.email)
        new_customer= Customer.objects.create(**validated_data,user=user)
        print(new_customer)
        '''Create a new Customer instance, given the accepted data.'''
        return new_customer

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
