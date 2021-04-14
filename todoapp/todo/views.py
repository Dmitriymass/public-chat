from django.shortcuts import render
from rest_framework import generics, views, permissions
# from rest_framework.response import Response
from todo.serializers import TodoDetailSerializer, TodoListSerializer, TodoCreateSerializer
from todo.models import Todo
from todo.permissions import IsOwnerOrReadOnly




class TodoCreateView(generics.CreateAPIView):
    serializer_class = TodoDetailSerializer
    queryset = Todo.objects.all()


class TodoListView(generics.ListAPIView):
    serializer_class = TodoListSerializer
    queryset = Todo.objects.all()


class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoDetailSerializer
    queryset = Todo.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )
