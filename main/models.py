from django.db import models
from django.contrib.auth.models import User
import uuid

class ProductEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    stocks = models.IntegerField()
    time = models.DateField(auto_now_add=True)

    @property
    def is_stock_ready(self):
        return self.stocks_intensity >= 1

# nama character, umur int, isHappy boolean

class Person(models.Model):
    nama = models.CharField(max_length=195)
    umur = models.IntegerField()
    isHappy = models.BooleanField()