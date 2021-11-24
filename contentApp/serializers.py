from rest_framework import serializers

from contentApp.models import *


class BookListSerializer(serializers.ModelSerializer):
    """
    Полный список книг
    """
    class Meta:
        model = Books
        fields = ("name", "year", "author", )


class BookSerializer(serializers.ModelSerializer):
    """
    Полная информация о книге
    """
    class Meta:
        model = Books
        fields = '__all__'


class AuthorListSerializer(serializers.ModelSerializer):
    """
    Полный список авторов
    """
    class Meta:
        model = Authors
        fields = ("name", "img")


class AuthorSerializer(serializers.ModelSerializer):
    """
    Полная информация об авторе
    """
    class Meta:
        model = Authors
        fields = '__all__'


"""
class SearchSerializer(serializers.ModelSerializer):

    search = serializers.CharField(
        max_length=50,
        style={'placeholder': 'Что же мы ищем?'}
    )
"""


class ReviewCreateSerializer(serializers.ModelSerializer):
    """
    Отзыв о книге, фильме
    """
    target = serializers.CharField(read_only=True)

    name = serializers.CharField(
        max_length=50,
        style={'placeholder': 'Ваше имя'}
    )
    shortReview = serializers.CharField(
        max_length=100,
        style={'placeholder': 'Кратко'}
    )
    text = serializers.CharField(
        max_length=10000,
        style={'base_template': 'textarea.html', 'placeholder': 'Отзыв', 'rows': 5}
    )

    class Meta:
        model = Reviews
        exclude = ("date", )
        # fields = '__all__'
