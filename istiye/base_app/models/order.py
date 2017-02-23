__author__ = 'Hakan Uyumaz'

from . import User, OrderItem, Restaurant
from .order_item import OrderItem
from django.db import models


class Order(models.Model):
    TYPE_LABELS = (('0', 'Alindi'), ('1', 'Hazirlaniyor'), ('2', 'Yola Cikti'), ('3', 'Tamamlandi'))
    type = models.CharField('Status', max_length=50, choices=TYPE_LABELS)
    order_owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    items = models.ManyToManyField(OrderItem, related_name="order")
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="orders")
    total_price = models.FloatField(default=0, null=False, blank=False)

    def __str__(self):
        return str(self.get_type_display()) + " - " + self.date.strftime("%d/%m%/%y - %H:%M")
