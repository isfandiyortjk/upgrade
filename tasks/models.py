
from django.db import models
from django.conf import settings
from projects.models import Project

class Task(models.Model):
 STATUS=[("todo","todo"),("in_progress","in_progress"),("done","done")]
 title=models.CharField(max_length=255)
 description=models.TextField(blank=True)
 project=models.ForeignKey(Project,on_delete=models.CASCADE)
 assigned_to=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
 status=models.CharField(max_length=20,choices=STATUS)
 priority=models.IntegerField(default=1)
 deadline=models.DateTimeField(null=True,blank=True)
 created_at=models.DateTimeField(auto_now_add=True)
