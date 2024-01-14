from django.shortcuts import render, redirect
from .models import Lesson
from apps.settings.models import Settings

def lesson_detail(request, lesson_id):
    settings = Settings.objects.latest('id')
    lesson = Lesson.objects.get(id=lesson_id)
    return render(request, 'lessons/lesson_detail.html', locals())