from django.db import models

from django.contrib.auth.models import AbtractUser

class User(models.Model):
    image = models.ImageField(upload_to='images/' ,null=True, blank=True)
    info = models.TextField()