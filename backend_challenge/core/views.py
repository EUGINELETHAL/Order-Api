from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import OrderSerializer
from .models import Order
from django.http import HttpResponse

# Create your views here.
class OrderListCreateAPIView(ListCreateAPIView):
    serializer_class = OrderSerializer
    
    def get_queryset(self):
        return Order.objects.all()

    
    def perform_create(self, serializer):
       serializer.save(customer=self.request.user)
      

def print_username(request):
    user=request.user
    print(user)
    return HttpResponse('good')



