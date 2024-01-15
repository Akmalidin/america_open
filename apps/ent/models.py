from django.db import models

# Create your models here.
class Slider(models.Model):
    bg_image = models.ImageField(verbose_name="Задний фон",upload_to="ent/slider/")
    image = models.ImageField(verbose_name="Картинка",upload_to="ent/slider/", blank=True, null=True)
    title = models.CharField(verbose_name="Загаловок",max_length=100)
    description = models.CharField(verbose_name='Описание', max_length=200)

class Subjects(models.Model):
    image = models.ImageField(verbose_name="Фото предмета", upload_to='ent/subjects/')
    title = models.CharField(verbose_name="Имя предмета", max_length=100)
    btn = models.BooleanField(verbose_name="Основной предмет", default=False)

class Test(models.Model):
    title = models.CharField(verbose_name="Название теста", max_length=100)
    description = models.TextField(verbose_name="Описание теста / Задачи")
    image = models.ImageField(upload_to="ent/test/", blank=True, null=True)
    