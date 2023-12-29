from django.shortcuts import render, get_object_or_404, redirect
from .models import Courses, Course, UserCourse
from apps.settings.models import Settings 
# Create your views here.

def courses(request):
    settings = Settings.objects.latest('id')
    courses = Courses.objects.all()
    return render(request, 'courses/courses.html', locals())

def show_course(request, slug):
    course = get_object_or_404(Courses, slug=slug)
    settings = Settings.objects.latest('id')
    return render(request, 'courses/course.html', locals()) 

def buy_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    # Проверка доступа пользователя к курсу
    if UserCourse.objects.filter(user=request.user, course=course).exists():
        user_course = UserCourse.objects.get(user=request.user, course=course)
        user_course.access_granted = True
        user_course.save()
    else:
        UserCourse.objects.create(user=request.user, course=course, access_granted=True)
    return redirect('my_courses')

def my_courses(request):
    user = request.user  # Убедитесь, что пользователь аутентифицирован
    user_courses = UserCourse.objects.filter(user=request.user, access_granted=True)
    settings = Settings.objects.latest('id')
    return render(request, 'courses/my_courses.html', locals())
