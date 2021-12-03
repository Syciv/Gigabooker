import unicodedata

from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from django.db.models.functions import Lower, Upper

from contentApp.models import Books, Authors, Reviews
from rest_framework.views import APIView
from rest_framework import generics, permissions
from contentApp.serializers import *


class BookListView(APIView):
    """
    Вывод списка книг
    """
    def get_queryset(self, request):
        books = Books.objects.all()
        serializer = BookListSerializer(books, many=True)
        return Response(serializer.data)


class BookDetailView(APIView):
    """
    Вывод всей информации о книге
    """
    def get(self, request, pk):
        book = Books.objects.get(id=pk)
        serializer = BookSerializer(book)

        return Response(serializer.data)


class AuthorListView(APIView):
    """
    Вывод списка авторов
    """
    def get(self, request):
        authors = Authors.objects.all()
        serializer = AuthorListSerializer(authors, many=True)
        return Response(serializer.data)


class AuthorDetailView(APIView):
    """
    Вывод всей информации об авторе
    """
    def get(self, request, pk):
        author = Authors.objects.get(id=pk)
        serializer = AuthorSerializer(author)

        return Response(serializer.data)


class ReviewCreateView(APIView):
    """
    Создание отзыва
    """
    def post(self, request):
        review = ReviewCreateSerializer(data=request.data)
        if review.is_valid():
            review.save()
        return Response(status=201)

