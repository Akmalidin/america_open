from django.shortcuts import render
from .models import Courses
from apps.settings.models import Settings 
# Create your views here.

def courses(request):
    settings = Settings.objects.latest('id')
    courses = Courses.objects.all()
    return render(request, 'courses/courses.html', locals())