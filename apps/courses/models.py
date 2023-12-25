from django.db import models

class Courses(models.Model):
    image = models.ImageField(upload_to='courses/', verbose_name='Фото курса')
    course_name = models.CharField(max_length=20, verbose_name='Название курса')
    course_description = models.TextField(verbose_name='Описание курса')
    time = models.IntegerField(verbose_name='Длительность курса', help_text='В месяцах: 12')
    course_price = models.IntegerField(verbose_name='Цена курса')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    
    
    def __str__(self):
        return self.course_name

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

class Course(models.Model):
    name = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return self.name
    