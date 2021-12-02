from django.contrib import admin
from django.urls import path, include

from mainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainApp.urls')),
    path('content/', include('contentApp.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include('contentApp.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('user/', include('usersApp.urls')),
]
