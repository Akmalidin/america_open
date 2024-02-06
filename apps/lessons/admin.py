from django.contrib import admin
from .models import Lesson, Moduls, Comment, Question, UserAnswer
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
    search_fields = ('title', 'module__title')
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('lesson', 'user', 'text', 'created_at')
    list_filter = ('lesson', 'user', 'created_at')
    search_fields = ('lesson', 'user')

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('moduls','question', 'answer')
    list_filter = ('question', 'moduls')
    search_fields = ('question', 'answer', 'option1', 'option2', 'option3', 'option4')
    list_editable = ('answer',)
    # filter_vertical = ('option1', 'option2', 'option3', 'option4')

@admin.register(UserAnswer)
class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'chosen_answer', 'is_correct')
    list_filter = ('user', 'question')
    search_fields = ('user', 'question', 'chosen_answer')