# Generated by Django 5.0.1 on 2024-03-01 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0033_remove_question_options_question_option1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useranswer',
            name='chosen_answer',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Выбранный ответ'),
        ),
        migrations.DeleteModel(
            name='Result',
        ),
    ]
