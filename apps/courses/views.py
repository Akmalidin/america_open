from django.shortcuts import render, get_object_or_404, redirect
from .models import Courses, UserCourse
from apps.settings.models import Settings 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.core.paginator import Paginator
from apps.lessons.models import Moduls, Lesson
from datetime import datetime, timedelta
# Create your views here.

def courses(request):
    settings = Settings.objects.latest('id')
    courses = Courses.objects.all()
    paginator = Paginator(courses, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'courses/courses.html', locals())

def show_course(request, slug):
    course = get_object_or_404(Courses, slug=slug)
    settings = Settings.objects.latest('id')
    modules = Moduls.objects.filter(course=course)
    lessons = Lesson.objects.filter(module__in=modules)
    if request.user.is_authenticated:
        if UserCourse.objects.filter(user=request.user, course=course).exists():
            user_course = UserCourse.objects.get(user=request.user, course=course)
            if not user_course.access_granted:
                return render(request, 'courses/fail.html', locals())
            else:
                return render(request, 'courses/course.html', locals())
        else:
            return render(request, 'courses/course.html', locals())
    else:
        return render(request, 'courses/course.html', locals())


@login_required
def buy_course(request, course_id):
    course = get_object_or_404(Courses, pk=course_id)
    user = request.user

    if UserCourse.objects.filter(user=user, course=course).exists():
        user_course = UserCourse.objects.get(user=user, course=course)
        if user_course.end_date < datetime.now():
            user_course.access_granted = False
            user_course.save()
        else:
            # Курс еще не закончился, доступ остается True
            pass
    else:
        end_date = datetime.now() + timedelta(days=course.time)
        UserCourse.objects.create(user=user, course=course, access_granted=True, end_date=end_date)
    
    return redirect('my_courses')

@login_required
def my_courses(request):
    user_courses = UserCourse.objects.filter(user=request.user, access_granted=True)
    settings = Settings.objects.latest('id')
    
    for user_course in user_courses:
        if user_course.end_date and user_course.end_date < datetime.now():
            user_course.access_granted = False
            user_course.save()
    
    paginator = Paginator(user_courses, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'courses/my_courses.html', locals())
