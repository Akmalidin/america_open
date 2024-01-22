from django.shortcuts import render, get_object_or_404, redirect
from .models import Courses, Course, UserCourse
from apps.settings.models import Settings 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.core.paginator import Paginator
from apps.lessons.models import Moduls, Lesson
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


def buy_course(request, course_id):
    course = get_object_or_404(Courses, pk=course_id)
    user = request.user
    
    if UserCourse.objects.filter(user=user, course=course).exists():
        user_course = UserCourse.objects.get(user=user, course=course)
        user_course.access_granted = False
        user_course.save()
    else:
        UserCourse.objects.create(user=user, course=course, access_granted=False)
    
    return redirect('my_courses')


@login_required
def my_courses(request):
    user = request.user  # Убедитесь, что пользователь аутентифицирован
    user_courses = UserCourse.objects.filter(user=request.user, access_granted=True)
    settings = Settings.objects.latest('id')
    paginator = Paginator(user_courses, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'courses/my_courses.html', locals())
