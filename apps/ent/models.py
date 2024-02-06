from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Slider(models.Model):
    bg_image = models.ImageField(verbose_name="Задний фон",upload_to="ent/slider/")
    image = models.ImageField(verbose_name="Картинка",upload_to="ent/slider/", blank=True, null=True)
    title = models.CharField(verbose_name="Загаловок",max_length=100)
    description = models.CharField(verbose_name='Описание', max_length=200)

    class Meta:
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайдеры'

class Subjects(models.Model):
    image = models.ImageField(verbose_name="Фото предмета", upload_to='ent/subjects/')
    title = models.CharField(verbose_name="Имя предмета", max_length=100)
    btn = models.BooleanField(verbose_name="Основной предмет", default=False)

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'
    def __str__(self):
        return self.title

    

class QuestionEnt(models.Model):
    moduls = models.ForeignKey(Subjects, on_delete=models.CASCADE, related_name='Вопросы_ENT', verbose_name="Предмет ENT")
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

class UserAnswerEnt(models.Model):
    question = models.ForeignKey('QuestionEnt', on_delete=models.CASCADE, verbose_name="Вопрос ENT")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    chosen_answer = models.CharField(max_length=255, verbose_name='Выбранный ответ')
    is_correct = models.BooleanField(verbose_name='Правильный ответ')

    def __str__(self):
        return f"Ответ пользователя {self.user.username} на вопрос {self.question}: {self.chosen_answer}"
    
    class Meta:
        verbose_name = 'Ответ на вопрос'
        verbose_name_plural = 'Ответы на вопросы'