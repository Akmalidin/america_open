from django.contrib import admin
from .models import Lesson, Moduls, Comment, Question
# Register your models here.
@admin.register(Moduls)
class ModulsAdmin(admin.ModelAdmin):
    list_display = ('title', 'course')
    list_filter = ['course']
    search_fields = ('title', 'course')
@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'module', 'created_at', 'updated_at')
    list_filter = ('title', 'module', 'created_at')
    search_fields = ('title', 'module')
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('lesson', 'user', 'text', 'created_at')
    list_filter = ('lesson', 'user', 'created_at')
    search_fields = ('lesson', 'user')

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')
    list_filter = ('question', 'answer')
    search_fields = ('question', 'answer')