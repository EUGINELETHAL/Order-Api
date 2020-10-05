from django.db import models


class TimeStampedModel(models.Model):
    added = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Order(TimeStampedModel):
    item = models.CharField(max_length=200, )
    amount = models.PositiveIntegerField
    customer = models.ForeignKey('authentication.User', on_delete=models.CASCADE)

    # def __str__(self):
    #     return f"Order: {self.id} -customer: {self.customer.}"

    class Meta:
        ordering = ["-added"]

# Create your models here.
