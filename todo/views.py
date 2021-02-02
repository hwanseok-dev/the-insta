from django.shortcuts import render
from rest_framework import viewsets  # add this
from .serializers import TodoSerializer, OwnerSerializer
from .models import Todo, User


class OwnerView(viewsets.ModelViewSet):
    serializer_class = OwnerSerializer
    queryset = Todo.objects.all()


class TodoView(viewsets.ModelViewSet):  # add this
    serializer_class = TodoSerializer  # add this
    queryset = Todo.objects.all()  # add this
