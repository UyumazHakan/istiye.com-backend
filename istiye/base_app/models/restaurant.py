__author__ = 'Hakan Uyumaz'

from django.db import models


class Restaurant(models.Model):
    TYPE_LABELS = (('0', 'Cin Restoranti'), ('1', 'Kebap Salonu'), ('2', 'Fast Food'))
    type = models.CharField('Status', max_length=50, choices=TYPE_LABELS)
    name = models.TextField(max_length=50, null=False, blank=False)
    place = models.TextField(max_length=50, null=False, blank=False)
    delivery_time = models.TextField(max_length=50, null=False, blank=False)
    photo = models.ImageField(upload_to='uploaded/restaurant_photos/%Y/%m/%d/%H/', null=True, blank=True)

    def __str__(self):
        return self.name
