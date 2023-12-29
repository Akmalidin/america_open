from django.contrib import admin
from .models import Courses, Course, UserCourse
# Register your models here.
@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ('id', 'course_name', 'course_description', 'course_price', 'image', 'created_at')
    list_display_links = ('id', 'course_name')
    list_filter = ('course_name', 'course_description', 'course_price', 'created_at')
    search_fields = ('course_name', 'course_description', 'course_price', 'created_at')
    list_editable = ('course_price',)
    prepopulated_fields = {'slug': ('course_name',)}
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name']
@admin.register(UserCourse)
class UserCourseAdmin(admin.ModelAdmin):
    list_display = ['user', 'course', 'access_granted']