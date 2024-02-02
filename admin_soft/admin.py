from django.contrib import admin

# Register your models here.
class MyAdminSite(admin.AdminSite):
    site_header = 'Моя Админ Панель'  # Заголовок, который будет отображаться в верхней части административной панели
    site_title = 'Моя Админ Панель'   # Название, которое будет отображаться во вкладке браузера

# Зарегистрируйте ваши модели с помощью вашего собственного класса административной панели
admin_site = MyAdminSite(name='myadmin')