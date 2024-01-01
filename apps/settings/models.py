from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Settings(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name = 'Название сайта'
    )
    description = models.TextField(
        verbose_name='Описание сайта'
    )
    logo = models.ImageField(
        upload_to='logo/',
        verbose_name='Логотип'
    )
    email = models.EmailField(
        verbose_name = 'Email '
    )
    phone = models.CharField(
        max_length=255,
        verbose_name='Номер телефона сайта'
    )
    instagram = models.URLField(
        verbose_name='Ссылка на Instagram',
        max_length=255, null=True, blank=True
    )
    tiktok = models.URLField(
        verbose_name='Ссылка на Tiktok',
        max_length=255, null=True, blank=True
    )
    youtube = models.URLField(
        verbose_name='Ссылка на Youtube',
        max_length=255, null=True, blank=True
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Основные Настройки сайта'
        verbose_name_plural = 'Основные Настройки сайта'

class Slider(models.Model):
    bg_image = models.ImageField(
        upload_to='slider/',
        verbose_name = 'Фоновое Изображение слайдера'
    )
    image = models.ImageField(
        upload_to='slider/',
        verbose_name = 'Изображение слайдера'
    )
    title = models.CharField(
        max_length=255,
        verbose_name = 'Загаловок слайдера'
    )
    suptitle = models.CharField(
        max_length=255,
        verbose_name='Подзаголовок слайдера 1',
        help_text='Уроки на кыргызском языке',
        blank=True, null=True,
    )
    suptitle2 = models.CharField(
        max_length=255,
        verbose_name='Подзаголовок слайдера 2',
        help_text='Возможность подготовиться в любое время',
        blank=True, null=True,
    )
    suptitle3 = models.CharField(
        max_length=255,
        verbose_name='Подзаголовок слайдера 3',
        help_text='99% наших выпусников являются стипендиатами',
        blank=True, null=True,
    )
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайдеры'


class Paket(models.Model):
    image = models.ImageField(
        upload_to='paket/',
        verbose_name='Фото тарифа'
    )
    title = models.CharField(
        max_length = 255,
        verbose_name = 'Название тарифа'
    )
    ent = models.IntegerField(
        verbose_name = 'Количество возможностей для сдачи ЕНТ:',
        help_text = 'В цифрах: 12'
    )
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Тариф'
        verbose_name_plural = 'Тарифы'

class Teachers(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name = 'Имя Преподавателя'
    )
    image = models.ImageField(
        upload_to='teachers/',
        verbose_name = 'Фото преподавателя'
    )
    description = models.TextField(
        verbose_name = 'Описание преподавателя'
    )
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'

# ===================== USER =============== #
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    school = models.CharField(max_length=100, blank=True, null=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    place_learn = models.CharField(max_length=255, verbose_name='Место учебы', blank=True, null=True)
    region = models.CharField(max_length=255, verbose_name='Область', blank=True, null=True)
    city = models.CharField(max_length=255, verbose_name='Город', blank=True, null=True)    
    clas = models.CharField(verbose_name='Класс', max_length=255, blank=True, null=True)
    birthday = models.CharField(max_length=255, verbose_name='Дата рождения', blank=True, null=True)
    # subject_1 = models.CharField(
    #     choices=subjects,
    #     verbose_name='Предметы'
    # )

    def __str__(self):
        return self.user.username
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'