from articles.views import TaskView, CreateUserView
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path

router = routers.SimpleRouter()
router.register('tasks', TaskView)
router.register('createUser', CreateUserView)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
              ] + router.urls
