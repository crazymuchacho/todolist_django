# Generated by Django 4.1.5 on 2023-02-23 09:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("todolist_app_startapp", "0006_alter_table_task_task_completed"),
    ]

    operations = [
        migrations.AlterField(
            model_name="table_task",
            name="task_create",
            field=models.DateTimeField(
                auto_now_add=True, help_text="Дата/время создания задачи"
            ),
        ),
    ]
