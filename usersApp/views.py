from django.shortcuts import render, redirect

# Create your views here.
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView

from usersApp.serializers import LogInSerializer


class LogInView(APIView):
    """
    Создание отзыва
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'usersApp/login.html'

    def get(self, request):
        serializer = LogInSerializer()
        return Response({'serializer': serializer})

