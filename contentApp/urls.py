from contentApp import views
from django.urls import path

from gigabooker import settings

urlpatterns = [
    path("books/", views.BookListView.as_view()),
    path("books/<int:pk>/", views.BookDetailView.as_view(), name='book'),
    path("authors/", views.AuthorListView.as_view()),
    path("authors/<int:pk>/", views.AuthorDetailView.as_view()),
    path("review/", views.ReviewCreateView.as_view()),
]
