from django.db import models
from django.core.validators import FileExtensionValidator 
from django.contrib.auth.models import User
from apps.courses.models import Courses
from django import forms
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
    video = models.FileField(
        upload_to="lessons/videos/",
        verbose_name="Видео",
        null=True,
        blank=True,
        validators=[FileExtensionValidator(allowed_extensions=['mp4'])],
    )
    video_url = models.TextField(
    verbose_name="Ссылка на видео",
    help_text="""Вставьте ссылку из ютуба код Embed
    <br>Например:
    <br>Перейдите на страницу видео на YouTube.
    <br>Нажмите на кнопку 'Поделиться' под видео.
    <br>Выберите 'Встроить'
    <br>Скопируйте предоставленный код и вставьте его в ваш HTML-код.""",
    blank=True, null=True
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

class Question(models.Model):
    moduls = models.ForeignKey(Moduls, on_delete=models.CASCADE, related_name='questions', verbose_name="Модуль")
    question = models.TextField(verbose_name='Вопрос')
    option1 = models.CharField(max_length=200, verbose_name='Вариант ответа 1')
    option2 = models.CharField(max_length=200, verbose_name='Вариант ответа 2')
    option3 = models.CharField(max_length=200, verbose_name='Вариант ответа 3')
    option4 = models.CharField(max_length=200, verbose_name='Вариант ответа 4')
    cat = (('Option1', 'Вариант ответа 1'), ('Option2', 'Вариант ответа 2'), ('Option3', 'Вариант ответа 3'), ('Option4', 'Вариант ответа 4'))
    answer = models.CharField(max_length=8, choices=cat)
    is_attempted = models.BooleanField(default=True, blank=True)
    
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.question


class UserAnswer(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='Вопросы', verbose_name="Вопрос")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Пользователи', verbose_name="Пользователь")
    chosen_answer = models.CharField(max_length=255, verbose_name='Выбранный ответ', null=True, blank=True)
    is_correct = models.BooleanField(verbose_name='Правильный ответ')

    def __str__(self):
        return f"Ответ пользователя {self.user.username} на вопрос {self.question}: {self.chosen_answer}"
    
    class Meta:
        verbose_name = 'Ответ на вопрос'
        verbose_name_plural = 'Ответы на вопросы'