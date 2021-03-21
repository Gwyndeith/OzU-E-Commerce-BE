from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    item_name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.item_name
