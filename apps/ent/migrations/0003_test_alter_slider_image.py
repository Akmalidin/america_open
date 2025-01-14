# Generated by Django 5.0.1 on 2024-01-18 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ent', '0002_slider_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название теста')),
                ('description', models.TextField(verbose_name='Описание теста / Задачи')),
                ('image', models.ImageField(blank=True, null=True, upload_to='ent/test/')),
            ],
        ),
        migrations.AlterField(
            model_name='slider',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='ent/slider/', verbose_name='Картинка'),
        ),
    ]
