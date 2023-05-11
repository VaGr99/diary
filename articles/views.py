from rest_framework import viewsets

from articles.models import Task
from articles.serializers import TaskSerializer


class TaskView(viewsets.ModelViewSet):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer

