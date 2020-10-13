from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import OrderSerializer
from .models import Order

# Create your views here.
class OrderListCreateAPIView(ListCreateAPIView):
    serializer_class = OrderSerializer
    
    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user)

    
    def perform_create(self, serializer):
       serializer.save(customer=self.request.user)


