from django.conf.urls import url, include
from django.conf.urls.static import static

from gigabooker import settings
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)