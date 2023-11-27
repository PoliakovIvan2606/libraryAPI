from django.db import models
from django.contrib.auth.models import AbstractUser
# Модель пользователя
class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField()
    date_joined = models.DateTimeField(auto_now_add=True)