from django.views.generic import ListView, DetailView
from django.conf.urls import url, include
from contentApp.models import Books, Authors
from contentApp import views
from django.conf.urls.static import static
from django.urls import path

from gigabooker import settings

urlpatterns = [
    path("books/", views.BookListView.as_view()),
    path("books/<int:pk>/", views.BookDetailView.as_view(), name='book'),
    path("authors/", views.AuthorListView.as_view()),
    path("authors/<int:pk>/", views.AuthorDetailView.as_view()),
    path("search=<sk>/", views.SearchListView.as_view()),
    # path("search/", views.SearchListView.as_view(), name='search_results'),
]
