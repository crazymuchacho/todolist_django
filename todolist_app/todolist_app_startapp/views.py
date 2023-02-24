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
