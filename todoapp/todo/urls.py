from rest_framework import routers
from django.contrib import admin
from django.urls import path, include
from todo.views import *

app_name = 'todo'
urlpatterns = [
    path('todo/create/', TodoCreateView.as_view()),
    path('all/', TodoListView.as_view()),
    path('todo/detail/<int:pk>/', TodoDetailView.as_view()),
]

# router = routers.DefaultRouter()
# router.register('api/todo', TodoViewSet, 'todo')
#
# urlpatterns = router.urls
