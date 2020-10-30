from django.urls import path,include
from .import views 
from .views import OrderListCreateAPIView


app_name = 'core'
urlpatterns = [
    path('oidc/', include('mozilla_django_oidc.urls')),
    path('customer', views.Customer_Create.as_view(), name='customer'),
    path('order', OrderListCreateAPIView.as_view(), name="order"),
   
]

