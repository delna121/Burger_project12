from msilib.schema import Class
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=12)

    def __str__(self):
        return  '{}'.format(self.name)
