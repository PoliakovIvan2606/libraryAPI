from django.contrib import admin
from .models import User

# Добавим-ка мы табличку пользователей в админку
admin.site.register(User)