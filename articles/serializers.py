from rest_framework import serializers
from django.contrib.auth.models import User

from articles.models import Task


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class TaskSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Task
        fields = '__all__'

    # Метод validate работает на уровне класса и обязательно должна вернуть validated_data
    def validate(self, attrs):
        if attrs['title'] == attrs['description']:
            raise serializers.ValidationError('field title must not be the same to field description')
        return attrs

    # Метод validate_<some field> работает c конкретным полем и обязательно должна вернуть <some field>
    def validate_title(self, title):
        if len(title) < 4:
            raise serializers.ValidationError(
                f'You inserted very small number characters {len(title)}. Must be 4 at least')
        return title


class PasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
