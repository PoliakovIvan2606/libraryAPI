from django.urls import path, include, re_path


urlpatterns = [
    # Создать пользователя
    path('', include('djoser.urls')),
    # Войти как пользователь и выйти, тоже как пользователь)))
    re_path(r'', include('djoser.urls.authtoken')),
]
