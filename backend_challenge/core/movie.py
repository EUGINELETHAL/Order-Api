import pytest
from django.contrib.auth.models import User
from hypothesis import given
from hypothesis import strategies as st
from hypothesis.extra.django import TestCase
from mixer.backend.django import mixer

from .models import Customer, Order


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient

    return APIClient()


@pytest.mark.django_db
def test_user_create():
    User.objects.create_user("john", "lennon@thebeatles.com", "johnpassword")
    assert User.objects.count() == 1


@pytest.mark.django_db
def test_customer_model():
    user = User.objects.create(username="eugine", email="ochungeugine@gmail.com")
    customer = Customer.objects.create(user=user, phone=733333)
    assert Customer.objects.count() == 1


@pytest.mark.django_db
def test_string_representation():
    user = User.objects.create(username="eugine", email="ochungeugine@gmail.com")
    customer = Customer.objects.create(user=user, phone=733333)
    assert str(customer) == "ochungeugine@gmail.com"


@pytest.mark.django_db
def test_authenticated_user_can_create_new_order(api_client):

    data = {"item": "books", "amount": 4, "customer": self.customer.id}
    response = self.client.post(self.url, data=data)
    print(response.data)
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(Order.objects.count(), 1)
