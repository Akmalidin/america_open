from django.contrib import admin
from .models import Lesson
# Register your models here.
@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'video_url', 'created_at', 'updated_at')