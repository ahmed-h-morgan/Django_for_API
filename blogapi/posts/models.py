from django.db import models

from django.conf import settings       # we import Django's settings to be able to refer to customized User stored in project/settings >> AUTH_USER_MODEL

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    