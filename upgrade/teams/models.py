
from django.db import models
from django.conf import settings

class Team(models.Model):
 name=models.CharField(max_length=255)
 owner=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
 members=models.ManyToManyField(settings.AUTH_USER_MODEL,related_name="teams")
