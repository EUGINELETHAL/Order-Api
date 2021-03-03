from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from .serializers import OrderSerializer, CustomerSerializer
from .models import Order,Customer
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
import africastalking
from.models import Order
username = "sandbox"    # use 'sandbox' for development in the test environment
api_key = "4b687203c43211be0e43105531bf92d7d8ad44d778bdfcf869988c465049291e"
africastalking.initialize(username, api_key)
sms = africastalking.SMS

def send_sms(order_id):
    """
  
    Task to send an sms notification when an order is
    successfully created.
    """
    order = Order.objects.get(id=order_id)
   
    message = f'Dear {order.customer.user} You have successfully placed an order.Your order ID is {order.id}.'
    response=sms.send(message,["+254728826517"])
    return response

class Customer_Create(APIView):
    permission_classes = [IsAuthenticated]
   
    """
   create a new customer
    """
    def post(self, request):
        
        serializer_context = {'request': request, 'user':self.request.user}
        serializer = CustomerSerializer(data=request.data,context=serializer_context)
        print(serializer)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Create your views here.
class OrderListCreateAPIView(ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    
    def get_queryset(self):
        try:
            customer=self.request.user.customer
        except Customer.DoesNotExist:
            raise NotFound('Please Create Customer Profile')
        return self.queryset.filter(customer=customer)
        

    
    def perform_create(self, serializer):
      f
        if serializer.is_valid(raise_exception=True):
            order=serializer.save()
            send_sms(order.id)
      
      




