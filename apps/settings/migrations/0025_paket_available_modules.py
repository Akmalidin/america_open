# Generated by Django 5.0.1 on 2024-02-19 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0024_remove_teachers_name_en_remove_teachers_name_ru'),
    ]

    operations = [
        migrations.AddField(
            model_name='paket',
            name='available_modules',
            field=models.IntegerField(default=0, verbose_name='Доступное количество модулей'),
        ),
    ]
