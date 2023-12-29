from django.db import models
from django.contrib.auth.models import User
class Courses(models.Model):
    image = models.ImageField(upload_to='courses/', verbose_name='Фото курса')
    course_name = models.CharField(max_length=20, verbose_name='Название курса')
    course_description = models.TextField(verbose_name='Описание курса')
    time = models.IntegerField(verbose_name='Длительность курса', help_text='В месяцах: 12')
    course_price = models.IntegerField(verbose_name='Цена курса')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    course = models.ForeignKey('Course', on_delete=models.PROTECT, null=True, blank=True)
    slug = models.SlugField(verbose_name='Авто URL', max_length=255, unique=True)
    def __str__(self):
        return self.course_name

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

class Course(models.Model):
    name = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reversed('course', kwargs={'course_id':self.pk})
    class Meta:
        verbose_name = 'Группа курса'
        verbose_name_plural = 'Группы курсов'

class UserCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    access_granted = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.user.username} - {self.course} - {self.access_granted}'
    class Meta:
        verbose_name = 'Разрешение для пользователя на курс'
        verbose_name_plural = 'Разрешения для пользователей на курсы'