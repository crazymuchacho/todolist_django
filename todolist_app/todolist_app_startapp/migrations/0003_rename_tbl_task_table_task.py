# Generated by Django 4.1.5 on 2023-02-22 16:10

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("todolist_app_startapp", "0002_alter_tbl_task_task_completed"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="tbl_Task",
            new_name="table_Task",
        ),
    ]
