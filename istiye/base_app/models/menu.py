__author__ = 'Hakan Uyumaz'

from .restaurant import Restaurant
from django.db import models


class Menu(models.Model):
    name = models.TextField(max_length=50, null=False, blank=False)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE,related_name="menus")

    def __str__(self):
        return str(self.restaurant) + " - " + self.name
