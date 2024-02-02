from django.contrib import admin
from .models import Courses, UserCourse
from modeltranslation.admin import TranslationAdmin
from modeltranslation.translator import register, TranslationOptions
# Register your models here.
@register(Courses)
class CoursesTranslationOptions(TranslationOptions):
    fields = ['course_description']

@admin.register(Courses)
class CoursesAdmin(TranslationAdmin):
    list_display = ('id', 'course_name', 'course_price', 'image', 'created_at')
    list_display_links = ('id', 'course_name')
    list_filter = ('course_name', 'course_price', 'created_at')
    search_fields = ('course_name', 'course_price', 'created_at')
    list_editable = ('course_price',)
    prepopulated_fields = {'slug': ('course_name',)}


class UserCourseAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'course', 'access_granted')  # Определение полей для отображения в списке объектов
    list_filter = ('user', 'course', 'access_granted')
admin.site.register(UserCourse, UserCourseAdmin)