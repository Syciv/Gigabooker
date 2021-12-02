import unicodedata

from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from django.db.models.functions import Lower, Upper

from contentApp.models import Books, Authors, Reviews
from rest_framework.views import APIView
from rest_framework import generics
from contentApp.serializers import *


class BookListView(APIView):
    """
    Вывод списка книг
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'contentApp/booksList.html'

    def get(self, request):
        books = Books.objects.all()
        return Response({'books': books})


class BookDetailView(APIView):
    """
    Вывод всей информации о книге
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'contentApp/book.html'

    def get(self, request, pk):
        book = Books.objects.get(id=pk)
        reviews = Reviews.objects.filter(target=pk)
        serializer = ReviewCreateSerializer(initial={'target': pk})
        # form = ReviewForm(initial={'target': pk})
        return Response({'book': book, 'reviews': reviews, 'serializer': serializer})

    def post(self, request, pk):
        serializer = ReviewCreateSerializer(data=request.data)
        # serializer.target = pk

        if serializer.is_valid():
            serializer.save(target=Books.objects.get(id=pk))

        return redirect('book', pk)
        # return HttpResponseRedirect('')  # Response(status=201)  #


class AuthorListView(APIView):
    """
    Вывод списка авторов
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'contentApp/authorsList.html'

    def get(self, request):
        authors = Authors.objects.all()
        return Response({'authors': authors})


class AuthorDetailView(APIView):
    """
    Вывод всей информации об авторе
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'contentApp/author.html'

    def get(self, request, pk):
        author = Authors.objects.get(id=pk)
        books = Books.objects.filter(author=pk)
        return Response({'author': author, 'author_books': books})


class ReviewCreateView(APIView):
    """
    Создание отзыва
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'contentApp/review.html'

    def post(self, request, pk):
        # review = get_object_or_404(Reviews, pk=pk)
        # serializer = ReviewCreateSerializer(review, data=request.data)
        review = ReviewCreateSerializer(data=request.data)
        if review.is_valid():
            review.save()

        return Response(status=201)


class SearchListView(APIView):
    """
    Вывод результатов поиска
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'contentApp/search.html'

    def get(self, request, sk):
        # Поиск без чуствительности к регистру не работает (особенности sqlite)
        books = Books.objects.filter(name__icontains=sk)
        authors = Authors.objects.filter(name__icontains=sk)
        return Response({'books': books, 'authors': authors, 'sk': sk})

