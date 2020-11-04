from django.test import TestCase
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Order, Customer
from rest_framework import status
from django.urls import reverse
from .import tasks
from .tasks import *

class OrderModelTest(TestCase):

    def test_string_representation(self):
        order= Order(id=2)
        self.assertEqual(str(order), "2" )

class CustomerModelTest(TestCase):

    def test_string_representation(self):
        user=User.objects.create(username="eugine",email="ochungeugine@gmail.com")
        customer= Customer.objects.create(user=user)
        self.assertEqual(str(customer), user.email)



class TestOrderAPI(APITestCase):
    url = '/api/v1/order'
    def setUp(self):
        self.username = "eugine"
        self.user = User.objects.create_user(self.username)
        self.client.force_authenticate(user=self.user)
        self.customer=Customer.objects.create(user=self.user,phone="0728825517")
       
       


    def test_authenticated_user_can_create_new_order(self):
        
        data= {
            'item': 'books',
            'amount': 4,
            'customer': self.customer.id
        }
        response=self.client.post(self.url, data=data)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)
        #  self.assertEqual(str(order), Order.id )
    

    def test_anonymous_user_cannot_create_order(self):
        self.client.force_authenticate(user=None)
        response=self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_order_with_no_item(self):
        data= {
            'item':'',
            'amount': 4,
            'customer': self.customer.id
        }
        response=self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_send_sms(self):
        data= {
            'item': 'books',
            'amount': 4,
            'customer': self.customer.id
        }
        response=self.client.post(self.url, data=data)
        message = 'Dear customer You have successfully placed an order.Your order ID is 1.'
        res =sms.send(message,["+254728826517"])
        recipients = res['SMSMessageData']['Recipients']
        assert len(recipients) == 1
        assert recipients[0]['status'] == 'Success'

    


class TestCreate_Customer(APITestCase):
    url = '/api/v1/customer'
    def setUp(self):
        self.username = "eugine"
        self.email='ochungeugine@gmil.com'
        self.user = User.objects.create_user(self.username)
        self.client.force_authenticate(user=self.user)
       
       


    def test_authenticated_user_can_create_customer(self):
        data= {
            'user':self.user,
            'phone': '0728826517'
        }
        
        response=self.client.post(self.url,data=data)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 1) 
        

    def test_anonymous_user_cannot_create_customer(self):
        self.client.force_authenticate(user=None)
        response=self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_crustomer_with_no_phone(self):
        data= {
            'user':self.user,
            'phone':''
        }
        response=self.client.post(self.url, data=data)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    
        


