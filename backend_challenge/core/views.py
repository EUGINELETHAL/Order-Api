from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import OrderSerializer
from .models import Order

# Create your views here.
class OrderListCreateAPIView(ListCreateAPIView):
    serializer_class = OrderSerializer
    
    def get_queryset(self):
        return Order.objects.all()

    
    def perform_create(self, serializer):
       serializer.save()


