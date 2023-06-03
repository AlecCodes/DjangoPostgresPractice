from django.shortcuts import render
from .models import Todo
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import TodoSerializer

# Create your views here.

class TodoViewSet(viewsets.ModelViewSet):
    ##main query for index route
    queryset = Todo.objects.all()
    #serializer class (like generator object?)
    serializer_class = TodoSerializer
    #optional permission class set permission level
    permission_classes = [permissions.AllowAny]