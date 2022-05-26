from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Client(models.Model):
    phone_number = PhoneNumberField()
    name = models.CharField(max_length=200)
    request_time = models.DateTimeField(auto_now_add=True)