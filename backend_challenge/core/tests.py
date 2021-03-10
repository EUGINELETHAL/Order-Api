import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient


@pytest.mark.django_db 
@pytest.fixture
def user_fixture():
   user= User.objects.create(
      username='john', email='lennon@thebeatles.com', password='johnpassword'
    
      )
   return user
@pytest.mark.django_db 
def test_user_create(user_fixture):
   assert User.objects.count() == 1
   #  )
   #  return user
   # @pytest.mark.parametrize(
   #    'user,phone,code, status_code', [
   #       (user_create,'+254728826517',None, 400),
   #       ('','+254728826517', 'strong_pass', 400),
   #       ('','+254728826517',None, 400),
   #       (user_create,'+254728826517', 'invalid_pass', 400),
   #       ('','+254728826517', 'strong_pass', 201),
   #    ])
   
@pytest.mark.django_db 
def test_customer_create(user_fixture):
   client = APIClient()
   url = '/api/v1/customer'
   client = APIClient()
   client.force_authenticate(user=user_fixture)
      
   data = {
         'phone': '+254728826517',
         'code': 'code',
         'user': user_fixture,
   }
      
   response = client.post(url, data=data)
   assert response.status_code == 201
@pytest.mark.django_db 
def test_anonymous_user_cannot_create_customer():
   client = APIClient()
   url ='/api/v1/customer'
   client.force_authenticate(user=None)
   response=client.get(url)
   assert response.status_code == 401
