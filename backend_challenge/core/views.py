from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import OrderSerializer
from .models import Order,Customer
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class OrderListCreateAPIView(ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Order.objects.all()

    
    def perform_create(self, serializer):
        serializer.save(customer=self.request.user.customer)
      

def print_username(request):
    user=request.user
    print(user)
    return HttpResponse('good')



