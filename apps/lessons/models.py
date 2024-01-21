from django.db import models
from django.contrib.auth.models import User
from apps.courses.models import Courses
# Create your models here.

class Moduls(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, verbose_name="Курс", related_name='modules')
    title = models.CharField(max_length=200, verbose_name="Название модуля")

    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name = 'Модуль'
        verbose_name_plural = 'Модули'
class Lesson(models.Model):
    module = models.ForeignKey(Moduls, on_delete=models.CASCADE, verbose_name="Модуль")
    title = models.CharField(max_length=200, verbose_name="Тема урока")
    description = models.TextField(verbose_name="Описание")
    video_url = models.TextField(
    verbose_name="Ссылка на видео",
    help_text="""Вставьте ссылку из ютуба код Embed
    <br>Например:
    <br>Перейдите на страницу видео на YouTube.
    <br>Нажмите на кнопку 'Поделиться' под видео.
    <br>Выберите 'Встроить'
    <br>Скопируйте предоставленный код и вставьте его в ваш HTML-код."""
)
    file = models.FileField(upload_to="lessons/files/", verbose_name="Файл для конспекта", null=True, blank=True)
    file2 = models.FileField(upload_to="lessons/files/", verbose_name="Файл для презентации", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Урок')
    text = models.TextField(verbose_name='Текст комментария')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f'{self.user.username} - {self.lesson.title}'
    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'

class CommentReply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Reply by {self.user.username} on {self.comment}'

    class Meta:
        ordering = ['-created_at']