from rest_framework import serializers
from .models import Order





class OrderSerializer(serializers.ModelSerializer):
    customer_phone = serializers.SerializerMethodField()
    # send_sms=serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ("item", "amount","customer_phone")

    def get_customer_phone(self, obj):
        return obj.customer.phone

    def get_send_sms(self, obj):
        sms = africastalking.SMS
        response = sms.send("Ordr created", ["+254728826517"])
        return response
        