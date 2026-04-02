
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet
r=DefaultRouter();r.register("",TaskViewSet)
urlpatterns=r.urls
