# Generated by Django 5.0.1 on 2024-02-22 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0028_remove_userprofile_selected_paket_userprofile_moduls'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='moduls',
        ),
    ]
