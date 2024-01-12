from django.urls import path
from django.utils.translation import gettext_lazy as _
from .views import courses, show_course, buy_course, my_courses
urlpatterns = [
    path('', courses, name='courses'),
    path(_('course/<slug:slug>/'), show_course, name='course'),
    path(_('buy/<int:course_id>/'), buy_course, name='buy_course'),
    path(_('my_courses/'), my_courses, name='my_courses'),
]
