from django.db import models

from django.urls import reverse

# Create your models here.

class Hit(models.Model):
	times = models.IntegerField()
	at = models.DateTimeField(auto_now_add=True)