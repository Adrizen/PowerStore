from django.db import models

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=7, verbose_name='Phone number')

class Item(models.Model):
    name = models.CharField(max_length=30)
    section = models.CharField(max_length=40)
    price = models.IntegerField()

    def __str(self):
        return f'The item {self.name} of section {self.section} costs ${self.price}'

class Order(models.Model):
    number = models.IntegerField()
    deliveryDate = models.DateField()
    delivered = models.BooleanField()