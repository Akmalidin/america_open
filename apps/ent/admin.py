from django.contrib import admin
from .models import Slider, Subjects, QuestionEnt, UserAnswerEnt
# Register your models here.
@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'bg_image', 'image', 'description')
@admin.register(Subjects)
class SubjectsAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'btn')

@admin.register(QuestionEnt)
class QuestionEntAdmin(admin.ModelAdmin):
    list_display = ('moduls','question', 'answer')
    list_filter = ('question', 'moduls')
    search_fields = ('question', 'answer', 'option1', 'option2', 'option3', 'option4')
    list_editable = ('answer',)
    # filter_vertical = ('option1', 'option2', 'option3', 'option4')

@admin.register(UserAnswerEnt)
class UserAnswerEntAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'is_correct')
    list_filter = ('user', 'question', 'question__moduls')
    search_fields = ('user', 'question', 'chosen_answer')