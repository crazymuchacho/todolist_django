from django_filters import rest_framework as dj_filters
from .models import table_Task


class TodolistFilterSet(dj_filters.FilterSet):
    """Набор фильров для представления для модели задач."""

    task = dj_filters.CharFilter(field_name="task", lookup_expr="icontains")
    is_active = dj_filters.BooleanFilter(field_name="task_is_Done")

    order_by_field = "ordering"

    class Meta:
        model = table_Task
        fields = [
            "task",
        ]
