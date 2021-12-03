from rest_framework import serializers
from contentApp.models import *


class ReviewSerializer(serializers.ModelSerializer):
    """
    Отзыв о книге
    """
    class Meta:
        model = Reviews
        fields = '__all__'


class BookListSerializer(serializers.ModelSerializer):
    """
    Полный список книг
    """
    class Meta:
        model = Books
        fields = ("name", "year", "author", "img")


class BookSerializer(serializers.ModelSerializer):
    """
    Полная информация о книге
    """
    reviews = ReviewSerializer(many=True)
    rating = serializers.SerializerMethodField()

    # Получение рейтинга книги в процентах
    def get_rating(self, ob):
        return ob.reviews.filter(recommend=True).count() / ob.reviews.all().count() * 100

    class Meta:
        model = Books
        fields = '__all__'


class AuthorListSerializer(serializers.ModelSerializer):
    """
    Полный список авторов
    """
    class Meta:
        model = Authors
        fields = ("name", "img", "birth", "death")


class AuthorSerializer(serializers.ModelSerializer):
    """
    Полная информация об авторе
    """
    books = BookListSerializer(many=True)

    class Meta:
        model = Authors
        fields = '__all__'


class ReviewCreateSerializer(serializers.ModelSerializer):
    """
    Отзыв о книге
    """
    class Meta:
        model = Reviews
        exclude = ("date", )

