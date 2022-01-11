from django.db import models
from django.utils import timezone


class Expense(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    price = models.FloatField()
    date = models.DateTimeField(default=timezone.now())
    description = models.TextField(default=None, blank=True, null=True)

    def __str__(self):
        return self.name

