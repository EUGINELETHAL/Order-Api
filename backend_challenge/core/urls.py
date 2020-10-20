from django.urls import path
from .views import OrderListCreateAPIView


app_name = 'core'
urlpatterns = [
    path('order', OrderListCreateAPIView.as_view(), name="list")
   
]

