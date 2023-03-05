from django.shortcuts import render
from todolist_app_startapp.models import table_Task
from django.views.generic import (
    DetailView,
    ListView,
    CreateView,
    UpdateView,
    View,
    DeleteView,
)
from rest_framework import viewsets, mixins

# from todolist_app_startapp.models import Article, Comment
from .serializers import TodolistSerializer
from .filters import TodolistFilterSet
from rest_framework.schemas.openapi import AutoSchema


# Create your views here.
class TaskListView(ListView):
    """Представление для отображения задач.

    .._ https://docs.djangoproject.com/en/4.1/ref/class-based-views/generic-display/#listview
    """

    context_object_name = "tasks_"
    queryset = table_Task.objects.all()
    # model = Cart
    template_name = "task_list.html"


class TaskCreateView(CreateView):
    """Представление для создания одной корзины.

    .._ https://docs.djangoproject.com/en/4.1/ref/class-based-views/generic-editing/#django.views.generic.edit.CreateView
    """

    model = table_Task
    fields = ["task", "task_is_Done"]
    template_name = "task_create.html"
    success_url = "/tasks/"


class TaskDeleteView(DeleteView):
    context_object_name = "task_del"
    model = table_Task
    fields = ["task", "task_is_Done"]
    template_name = "task_delete.html"
    success_url = "/tasks/"


class TaskUpdateView(UpdateView):
    """Представление для создания одной корзины.

    .._ https://docs.djangoproject.com/en/4.1/ref/class-based-views/generic-editing/#django.views.generic.edit.CreateView
    """

    model = table_Task
    fields = ["task", "task_is_Done"]
    template_name = "task_edit.html"
    success_url = "/tasks/"


class TodolistViewSet(
    mixins.ListModelMixin,  # GET /articles
    mixins.CreateModelMixin,  # POST /articles
    mixins.RetrieveModelMixin,  # GET /articles/1
    mixins.DestroyModelMixin,  # DELETE /articles/1
    mixins.UpdateModelMixin,  # PUT /articles/1
    viewsets.GenericViewSet,
):
    queryset = table_Task.objects.all().order_by("-id")
    serializer_class = TodolistSerializer

    filterset_class = TodolistFilterSet

    #    schema = AutoSchema(
    #       tags=['Articles'],
    #      component_name='Article',
    #     operation_id_base='Article',
    # )

    # pagination_class = None
    # permission_classes = [IsAuthenticated]

    # def get_serializer_class(self):
    #     if self.action == "list":
    #         return NonModelSerializer
    #     return ArticleSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
