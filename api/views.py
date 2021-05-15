from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer

from .models import Task

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def delete(self, request):
        Task.objects.all().delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

