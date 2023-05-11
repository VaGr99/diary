from rest_framework import serializers
from django.contrib.auth.models import User

from articles.models import Task


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class TaskSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Task
        fields = '__all__'
