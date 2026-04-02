
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet
r=DefaultRouter();r.register("",ProjectViewSet)
urlpatterns=r.urls
