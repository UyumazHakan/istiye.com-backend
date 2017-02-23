__author__ = 'Hakan Uyumaz'

from .menu import Menu
from django.db import models


class Menu_Category(models.Model):
    name = models.TextField(max_length=50, null=False, blank=False)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name="categories")


    def __str__(self):
        return str(self.menu.restaurant) + " - " + self.name
