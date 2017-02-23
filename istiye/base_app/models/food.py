__author__ = 'Hakan Uyumaz'

from .menu_category import Menu_Category
from django.db import models


class Food(models.Model):
    name = models.TextField(max_length=50, null=False, blank=False)
    price= models.FloatField(null=False, blank=False)
    photo = models.ImageField(upload_to='uploaded/food_photos/%Y/%m/%d/%H/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    menu_category = models.ForeignKey(Menu_Category, on_delete=models.CASCADE, related_name="foods")


    def __str__(self):
        return str(self.menu_category.menu.restaurant) + " - " + self.name
