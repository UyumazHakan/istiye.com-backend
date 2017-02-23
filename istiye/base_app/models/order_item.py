__author__ = 'Hakan Uyumaz'

from . import Food
from django.db import models
from ..utils import generate_token



class OrderItem(models.Model):
    food = models.ForeignKey(Food, related_name="order_items")
    amount = models.IntegerField(default=1, null=False, blank=False)

    def __str__(self):
        return str(self.amount) + str(self.food)
