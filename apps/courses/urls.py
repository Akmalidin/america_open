from django.urls import path
from .views import courses, show_course, buy_course, my_courses
urlpatterns = [
    path('', courses, name='courses'),
    path('course/<slug:slug>/', show_course, name='course'),
    path('buy/<int:course_id>/', buy_course, name='buy_course'),
    path('my_courses/', my_courses, name='my_courses'),
]
