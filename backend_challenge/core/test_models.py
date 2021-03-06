
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Order, Customer
from rest_framework import status
from django.urls import reverse
from .import tasks
from .tasks import *
from rest_framework.test import APITestCase


class TestCustomer(APITestCase):
    """ class to test the profile models"""

    def setUp(self):
        """ Setup some code that is used by the unittests"""
        self.email = 'serem@gmail.com'
        self.username = 'testing'
        self.password = 'jcbsdhcvshucj!!'

        # create a user that will be logged in
        self.user = User.objects.create_user(
            self.username, self.email, self.password)
        self.customer=Customer.objects.create(user=self.user,phone='0728826517')
        

    def test_customer_creation(self):
        self.assertEqual(self.customer.__str__(),
            "serem@gmail.com"
        )
        self.assertTrue(isinstance(self.customer,Customer))


       