
from rest_framework.viewsets import ModelViewSet
from .models import Task
from rest_framework import serializers

class TaskSerializer(serializers.ModelSerializer):
 class Meta:
  model=Task
  fields="__all__"

class TaskViewSet(ModelViewSet):
 queryset=Task.objects.all()
 serializer_class=TaskSerializer
 filterset_fields=["status","priority"]
 search_fields=["title"]
