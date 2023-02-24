from django.db import models
from django.conf import settings
from django_extensions.db.models import TimeStampedModel
import datetime


# Create your models here.


class table_Task(models.Model):
    """Задачи в todolist"""

    task = models.CharField(max_length=1024, help_text="Формулировка задачи")
    task_is_Done = models.BooleanField(default=False, help_text="Задача выполнена")
    task_create = models.DateTimeField(
        auto_now_add=True, help_text="Дата/время создания задачи"
    )
    task_completed = models.DateTimeField(
        blank=True, null=True, help_text="Дата/время завершения задачи"
    )

    def save(self, *args, **kwargs) -> None:
        """Переопределение сохранения.

        Убирается галочка активности корзины если нет привязанного пользователя.
        """
        if self.task_is_Done is False:
            self.task_completed = None
        else:
            time_now = datetime.datetime.utcnow()
            self.task_completed = time_now
        return super().save(*args, **kwargs)

    def __str__(self):
        """переопределение строкового представления объекта."""
        return f"Task {self.id}|{self.task}|{self.task_is_Done}|{self.task_create}|{self.task_completed}"
