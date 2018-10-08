from django.db import models
from django.utils import timezone


class List(models.Model):
    text = models.CharField(max_length=100)


class ListItem(models.Model):
    text = models.CharField(max_length=100)
    parent = models.ForeignKey(List, on_delete=models.CASCADE)
