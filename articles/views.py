from rest_framework import viewsets, views

from articles.models import Task
from articles.serializers import TaskSerializer, UserSerializer
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import CreateModelMixin
from django.contrib.auth import get_user_model
from .serializers import UserSerializer


class TaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]


class CreateUserView(CreateModelMixin, GenericViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
