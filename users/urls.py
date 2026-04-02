
from rest_framework.routers import DefaultRouter
from .views import UserViewSet
r=DefaultRouter();r.register("",UserViewSet)
urlpatterns=r.urls
