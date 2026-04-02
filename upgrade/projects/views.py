
from rest_framework.viewsets import ModelViewSet
from .models import Project
from rest_framework import serializers

class ProjectSerializer(serializers.ModelSerializer):
 class Meta:
  model=Project
  fields="__all__"

class ProjectViewSet(ModelViewSet):
 queryset=Project.objects.all()
 serializer_class=ProjectSerializer
 filterset_fields=["team","archived"]
