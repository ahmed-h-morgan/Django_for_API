from django.db import models

from django.contrib.auth.models import AbstractUser           # the AbstractUser is the model to use for customizing users

# Create your models here.

class CustomUser(AbstractUser):
    name = models.CharField(null=True, blank=True, max_length=100)
