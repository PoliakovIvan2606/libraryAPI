"""
URL configuration for libraryAPI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from books import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # url для работы с user-ами
    path('book/api/v1/', include('users.urls')),
    # для работы с книгами
    path('book/api/v1/list/', views.BooksAPIList.as_view(), name='list'),
    path('book/api/v1/create/', views.BookAPICreate.as_view(), name='create'),
    path('book/api/v1/<int:pk>', views.BookAPI.as_view(), name='RUD'),
]