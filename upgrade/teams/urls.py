
from rest_framework.routers import DefaultRouter
from .views import TeamViewSet
r=DefaultRouter();r.register("",TeamViewSet)
urlpatterns=r.urls
