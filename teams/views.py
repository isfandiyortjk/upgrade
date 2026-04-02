
from rest_framework.viewsets import ModelViewSet
from .models import Team
from rest_framework import serializers,permissions

class TeamSerializer(serializers.ModelSerializer):
 class Meta:
  model=Team
  fields="__all__"

class TeamViewSet(ModelViewSet):
 queryset=Team.objects.all()
 serializer_class=TeamSerializer
 permission_classes=[permissions.IsAuthenticated]
