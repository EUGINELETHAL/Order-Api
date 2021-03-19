from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import APIException, NotFound, ValidationError

from .models import Customer, Order


class CustomerProfileUnavailable(APIException):
    status_code = 400
    default_detail = "Create CustomerProfile"
    default_code = "service_unavailable"


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ("phone", "code")


class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ("item", "amount", "customer")


    def create(self, validated_data):
        request = self.context.get("request", None)
        if request is None:
            return False
        if "customer" not in validated_data:
            try:
                validated_data["customer"] = request.user.customer
            except Customer.DoesNotExist:
                raise CustomerProfileUnavailable()

        """Create a new Customer instance, given the accepted data."""

        return Order.objects.create(**validated_data)
