# Generated by Django 4.1.5 on 2023-02-22 16:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("todolist_app_startapp", "0005_alter_table_task_task_completed"),
    ]

    operations = [
        migrations.AlterField(
            model_name="table_task",
            name="task_completed",
            field=models.DateTimeField(
                blank=True, help_text="Дата/время завершения задачи", null=True
            ),
        ),
    ]
