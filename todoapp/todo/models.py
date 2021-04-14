from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Todo(models.Model):
    id = models.PositiveIntegerField
    email = models.CharField(max_length=100)
    text = models.CharField(max_length=300, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

