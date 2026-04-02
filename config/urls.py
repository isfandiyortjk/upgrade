
from django.urls import path,include
from drf_spectacular.views import SpectacularAPIView,SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns=[
path("api/auth/login/",TokenObtainPairView.as_view()),
path("api/auth/refresh/",TokenRefreshView.as_view()),
path("api/users/",include("users.urls")),
path("api/teams/",include("teams.urls")),
path("api/projects/",include("projects.urls")),
path("api/tasks/",include("tasks.urls")),
path("api/schema/",SpectacularAPIView.as_view(),name="schema"),
path("api/docs/",SpectacularSwaggerView.as_view(url_name="schema")),
]
