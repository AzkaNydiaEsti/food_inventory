from django.contrib.auth.models import User

# Create your models here.
from django.db import models

class Barang(models.Model):
    name = models.CharField(max_length=255)
    quality = models.TextField()
    type = models.CharField(max_length=105)
    description = models.TextField()
    amount = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)