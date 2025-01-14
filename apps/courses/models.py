from django.db import models
from django.contrib.auth.models import User

class Courses(models.Model):
    image = models.ImageField(upload_to='courses/', verbose_name='Фото курса')
    course_name = models.CharField(max_length=20, verbose_name='Название курса')
    course_description = models.TextField(verbose_name='Описание курса')
    time = models.IntegerField(verbose_name='Длительность курса', help_text='В месяцах: 12')
    course_price = models.IntegerField(verbose_name='Цена курса')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    slug = models.SlugField(verbose_name='Авто URL', max_length=255, unique=True)
    def __str__(self):
        return self.course_name

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class UserCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, verbose_name='Курсы')
    access_granted = models.BooleanField(verbose_name='Разрешено', default=False)
    phone_number = models.CharField(verbose_name="Номер телефона",max_length=20, blank=True, null=True)
    end_date = models.DateField(null=True, blank=True, verbose_name='Дата окончания курса')
    def __str__(self):
        return f"{self.user.username} ({self.phone_number})"

    def save(self, *args, **kwargs):
        from apps.settings.models import UserProfile
        if not self.pk:  # Проверяем, создается ли объект или обновляется
            self.access_granted = False  # Устанавливаем значение по умолчанию только при создании объекта
            user_profile = UserProfile.objects.get(user=self.user)
            self.phone_number = user_profile.phone_number
        super().save(*args, **kwargs)
    class Meta:
        verbose_name = 'Разрешение на курс'
        verbose_name_plural = 'Разрешения на курсы'