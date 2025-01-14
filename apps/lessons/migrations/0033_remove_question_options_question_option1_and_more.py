# Generated by Django 5.0.1 on 2024-02-13 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0032_remove_question_option1_remove_question_option2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='options',
        ),
        migrations.AddField(
            model_name='question',
            name='option1',
            field=models.CharField(default=1, max_length=200, verbose_name='Вариант ответа 1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='option2',
            field=models.CharField(default=1, max_length=200, verbose_name='Вариант ответа 2'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='option3',
            field=models.CharField(default=1, max_length=200, verbose_name='Вариант ответа 3'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='option4',
            field=models.CharField(default=1, max_length=200, verbose_name='Вариант ответа 4'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.CharField(choices=[('Option1', 'Вариант ответа 1'), ('Option2', 'Вариант ответа 2'), ('Option3', 'Вариант ответа 3'), ('Option4', 'Вариант ответа 4')], max_length=8),
        ),
        migrations.AlterField(
            model_name='question',
            name='is_attempted',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]
