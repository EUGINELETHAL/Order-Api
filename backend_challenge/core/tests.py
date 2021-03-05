import json
import pytest
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Order, Customer
from rest_framework import status
from django.urls import reverse
from .import tasks
from .tasks import *
from rest_framework.test import APITestCase

# class OrderModelTest(TestCase):

#     def test_string_representation(self):
#         order= Order(id=2)
#         self.assertEqual(str(order), "2" )
@pytest.mark.django_db
def test_user_create():
  User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
  assert User.objects.count() == 1


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
            'phone': '+254728826517',
            'code': '0728826517'
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
            'phone':'',
            'code': '0728826517'
            
        }
        response=self.client.post(self.url, data=data)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    def test_create_customer_with_no_code(self):
        data= {
            'user':self.user,
            'code':'',
            'phone': '+254728826517',
            
        }
        response=self.client.post(self.url, data=data)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)



   



class TestOrderAPI(APITestCase):
    url = '/api/v1/order'
    def setUp(self):
        self.username = "eugine"
        self.user = User.objects.create_user(self.username)
        self.client.force_authenticate(user=self.user)
        self.customer=Customer.objects.create(user=self.user,phone="+254728826517")
       
       


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
        print(res)
        recipients = res['SMSMessageData']['Recipients']
        assert len(recipients) == 1
        assert recipients[0]['status'] == 'Success'
    
    def test_string_representation(self):
        order=Order.objects.create(item="books", amount=4, customer=self.customer)
        self.assertEqual(str(order), "3" )

    def test_list_orders(self):
        response = self.client.get(self.url)
        self.assertTrue(len(json.loads(response.content)) == Order.objects.count())

# @pytest.mark.django_db
# def test_send_new_event_service_called(
#    mocker, default_event_data, api_client
# ):
#    mock_send_new_event = mocker.patch(
#        'service.ThirdPartyService.send_new_event'
#    )
#    response = api_client.post(
#        'create-service', data=default_event_data
#    )

#    assert response.status_code == 201
#    assert response.data['id']
#    mock_send_new_event.assert_called_with(
#        event_id=response.data['id']
#    )
    



    
        


