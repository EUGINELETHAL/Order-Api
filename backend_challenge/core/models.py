from django.db import models
from mozilla_django_oidc.auth import OIDCAuthenticationBackend
from django.contrib.auth.models import User

class Customer(models.Model):
    phone = models.CharField('phone', max_length=12)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.email
    



class TimeStampedModel(models.Model):
    added = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Order(TimeStampedModel):
    item = models.CharField(max_length=200, )
    amount = models.PositiveIntegerField(default=1)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)

    def __str__(self):
        return f"Order: {self.id} -customer: {self.customer}"

    class Meta:
        ordering = ["-added"]




