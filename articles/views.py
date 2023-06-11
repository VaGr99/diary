from rest_framework import viewsets, views

from articles.models import Task
from articles.serializers import TaskSerializer, UserSerializer
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import CreateModelMixin
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .serializers import UserSerializer, PasswordSerializer




class TaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]


class CreateUserView(CreateModelMixin, GenericViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    @action(detail=True, methods=['put', 'patch'])
    def set_password(self, request, pk=None):
        if pk is None:
            return Response({f'{request.method}': 'Method is not allowed'})
        try:
            user = User.objects.get(pk=pk)
        except:
            return Response({f'{request.method}': 'There isn`t user instance'})
        serializer = PasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user.set_password(serializer.validated_data['password'])
        user.save()
        return Response({'change': 'Password was set'})


