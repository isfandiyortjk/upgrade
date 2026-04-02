
from django.db import models
from teams.models import Team
class Project(models.Model):
 name=models.CharField(max_length=255)
 team=models.ForeignKey(Team,on_delete=models.CASCADE)
 archived=models.BooleanField(default=False)
