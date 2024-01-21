# Generated by Django 4.2.8 on 2024-01-13 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lessons", "0002_alter_comment_lesson"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="homework",
            name="lesson",
        ),
        migrations.RemoveField(
            model_name="submission",
            name="homework",
        ),
        migrations.RemoveField(
            model_name="submission",
            name="user",
        ),
        migrations.AddField(
            model_name="lesson",
            name="description",
            field=models.TextField(default=1, verbose_name="Описание"),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name="Comment",
        ),
        migrations.DeleteModel(
            name="Homework",
        ),
        migrations.DeleteModel(
            name="Submission",
        ),
    ]