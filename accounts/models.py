from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class register(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)

    def __str__(self):
        return self.username