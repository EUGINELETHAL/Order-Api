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
        
        serializer_context = {'request': request, 'user':self.request.user}
        serializer = CustomerSerializer(data=request.data,context=serializer_context)
        print(serializer)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
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
      
        if serializer.is_valid(raise_exception=True):
            serializer.save()
      
      




