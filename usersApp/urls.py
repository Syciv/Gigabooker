from usersApp import views
from django.urls import path

from gigabooker import settings

urlpatterns = [
    path("login/", views.LogInView.as_view()),
    # path("search/", views.SearchListView.as_view(), name='search_results'),
]