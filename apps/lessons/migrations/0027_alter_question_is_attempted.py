# Generated by Django 5.0.1 on 2024-02-01 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0026_useranswer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='is_attempted',
            field=models.BooleanField(default=True),
        ),
    ]
