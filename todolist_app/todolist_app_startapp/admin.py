from django.contrib import admin
from todolist_app_startapp.models import table_Task


# Register your models here.


@admin.register(table_Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "task",
        "task_is_Done",
        "task_create",
        "task_completed",
    )

    search_fields = ("task", "task_create") # по каким полям будет производиться поиск
