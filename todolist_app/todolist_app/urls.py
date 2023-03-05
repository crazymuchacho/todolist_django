"""todolist_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from todolist_app_startapp.views import (
    TaskListView,
    TaskCreateView,
    TaskDeleteView,
    TaskUpdateView,
)
from rest_framework.routers import DefaultRouter
from todolist_app_startapp.views import TodolistViewSet
from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view


urlpatterns = [
    path("admin/", admin.site.urls),
    path("tasks/", TaskListView.as_view()),
    path("task_create/", TaskCreateView.as_view(), name="task_crt"),
    path("task_delete/<int:pk>/delete", TaskDeleteView.as_view(), name="task_delete"),
    path("task/<int:pk>/edit", TaskUpdateView.as_view(), name="task_edit"),
    path("api/", include("todolist_app_startapp.urls")),
]


# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path("tasks/", TaskListView.as_view()),
#     path("task_create/", TaskCreateView.as_view(), name="task_crt"),
#     path("task_delete/<int:pk>/delete", TaskDeleteView.as_view(), name="task_delete"),
#     path("task/<int:pk>/edit", TaskUpdateView.as_view(), name="task_edit"),
# ]
