from django.contrib.auth.models import User
from rest_framework import serializers


class LogInSerializer(serializers.ModelSerializer):
    """
    Вход пользователя
    """
    username = serializers.CharField(
        max_length=150,
        style={'placeholder': 'Логин'}
    )
    password = serializers.CharField(
        max_length=50,
        style={'input_type': 'password', 'placeholder': 'Пароль'}
    )

    class Meta:
        model = User
        fields = ['username', 'password']