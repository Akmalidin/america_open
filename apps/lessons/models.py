from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Lesson(models.Model):
    title = models.CharField(max_length=200, verbose_name="Тема урока")
    description = models.TextField(verbose_name="Описание")
    video_url = models.URLField(verbose_name="Ссылка на видео")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
