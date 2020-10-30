from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from .serializers import OrderSerializer, CustomerSerializer
from .models import Order,Customer
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# import africastalking
# username = "sandbox"    # use 'sandbox' for development in the test environment
# api_key = "c24b10b049468747684e01f846e1a7420e106584c144d187b62d39fe667b6a78"
# africastalking.initialize(username, api_key)


class Customer_Create(APIView):
    permission_classes = [IsAuthenticated]
   
    """
   create a new customer
    """
    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Create your views here.
class OrderListCreateAPIView(ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Order.objects.all()

    
    def perform_create(self, serializer):
        serializer.save(customer=self.request.user.customer)
      

# def send_sms(request):
#     sms = africastalking.SMS
#     message = f'Dear {order.customer.email} You have successfully placed an order.Your order ID is {order.id}.'
#     sms.send(message,["+254728826517"])
#     return response




#from celery import task
# from django.core.mail import send_mail
# from .models import Order
# @task
# def order_created(order_id):
# """
# [ 265 ]Building an Online Shop
# Task to send an e-mail notification when an order is
# successfully created.
# """
# order = Order.objects.get(id=order_id)
# subject = f'Order nr. {order.id}'
# message = f'Dear {order.first_name},\n\n' \
# f'You have successfully placed an order.' \
# f'Your order ID is {order.id}.'
# mail_sent = send_mail(subject,
# message,
# 'admin@myshop.com',
# [order.email])
# return mail_sent



