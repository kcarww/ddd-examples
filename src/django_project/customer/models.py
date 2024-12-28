from django.db import models
from uuid import uuid4
# Create your models here.

class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    rewards_points = models.IntegerField(default=0)

    class Meta:
        db_table = 'customer'

    def __str__(self):
        return self.name