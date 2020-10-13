from rest_framework import serializers
from .models import Order
from backend_challenge.authentication.models  import  User

class OrderUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("email", "phone")


class OrderSerializer(serializers.ModelSerializer):
    user = OrderUserSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ("customer", "item", "amount", )
 