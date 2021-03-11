import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from .models import Customer, Order
from .tasks import send_sms


@pytest.mark.django_db
@pytest.fixture
def user_fixture():
    user = User.objects.create(
        username="john", email="lennon@thebeatles.com", password="johnpassword"
    )
    return user


@pytest.mark.django_db
def test_user_create(user_fixture):
    assert User.objects.count() == 1


@pytest.mark.django_db
@pytest.mark.django_db
def test_customer_create(user_fixture):
    client = APIClient()
    url = "/api/v1/customer"
    client = APIClient()
    client.force_authenticate(user=user_fixture)

    data = {
        "phone": "+254728826517",
        "code": "code",
        "user": user_fixture,
    }

    response = client.post(url, data=data)
    assert response.status_code == 201
    assert Customer.objects.count() == 1


@pytest.mark.django_db
def test_anonymous_user_cannot_create_customer():
    client = APIClient()
    url = "/api/v1/customer"
    client.force_authenticate(user=None)
    response = client.get(url)
    assert response.status_code == 401


@pytest.mark.django_db
def test_customer_create_invalid_phone(user_fixture):
    client = APIClient()
    url = "/api/v1/customer"
    client = APIClient()
    client.force_authenticate(user=user_fixture)

    data = {
        "phone": "0728826517",
        "code": "code",
        "user": user_fixture,
    }

    response = client.post(url, data=data)
    assert response.status_code == 400


@pytest.mark.django_db
def test_customer_create_no_phone(user_fixture):
    client = APIClient()
    url = "/api/v1/customer"
    client = APIClient()
    client.force_authenticate(user=user_fixture)

    data = {
        "phone": "",
        "code": "code",
        "user": user_fixture,
    }

    response = client.post(url, data=data)
    assert response.status_code == 400


@pytest.mark.django_db
def test_customer_create_no_code(user_fixture):
    client = APIClient()
    url = "/api/v1/customer"
    client = APIClient()
    client.force_authenticate(user=user_fixture)

    data = {
        "phone": "",
        "code": "",
        "user": user_fixture,
    }

    response = client.post(url, data=data)
    assert response.status_code == 400


@pytest.mark.django_db
def test_order_create(user_fixture):
    client = APIClient()
    url = "/api/v1/order"
    client = APIClient()
    client.force_authenticate(user=user_fixture)
    customer = Customer.objects.create(
        user=user_fixture, phone="+254728826517", code="5665"
    )
    data = {"item": "books", "amount": 4, "customer": customer}
    response = client.post(url, data=data)
    assert response.status_code == 201
    assert Order.objects.count() == 1


@pytest.mark.django_db
def test_send_new_event_service_called(mocker, user_fixture):
    client = APIClient()
    url = "/api/v1/order"
    client = APIClient()
    client.force_authenticate(user=user_fixture)
    customer = Customer.objects.create(
        user=user_fixture, phone="+254728865507", code="5665"
    )
    data = {"item": "books", "amount": 4, "customer": customer}
    response = client.post(url, data=data)
    assert response.status_code == 201
    order=Order.objects.get(customer=customer)
    mock_send_new_event = mocker.patch("backend_challenge.core.tasks.send_sms",
		    				return_value={'SMSMessageData': {'Message': 'Sent to 1/1 Total Cost: KES 0.8000', 'Recipients': [{'statusCode': 101, 'number': '+254728865507', 'cost': 'KES 0.8000', 'status': 'Success', 'messageId': 'ATXid_415eabf3cb8623da7f6aa2b2c79981c9'}]}}
		)
    
    mock_send_new_event(order_id=order.id)
    mock_send_new_event.assert_called_once_with(
       order_id=order.id
   )

  
    
