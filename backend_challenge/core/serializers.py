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

    # def validate(self, data):
    #     if not data.get('customer'):
    #         raise serializers.ValidationError(
    #                 'Please Update your profile details')
    #     return data

    #     return data
    #  def validate(self, data):
    #     data = super().validate(data)
    #     event = self.context['request'].event

    #     full_data = self.to_internal_value(self.to_representation(self.instance)) if self.instance else {}
    #     full_data.update(data)

    #     Event.clean_dates(data.get('date_from'), data.get('date_to'))
    #     Event.clean_presale(data.get('presale_start'), data.get('presale_end'))

    #     SubEvent.clean_items(event, [item['item'] for item in full_data.get('subeventitem_set', [])])
    #     SubEvent.clean_variations(event, [item['variation'] for item in full_data.get('subeventitemvariation_set', [])])
    #     return data

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
