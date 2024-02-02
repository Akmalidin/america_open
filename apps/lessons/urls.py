from django.urls import path
from . import views

urlpatterns = [
    path('lesson/<int:lesson_id>/', views.lesson_detail, name='lesson_detail'),
    path('add_comment_reply/<int:lesson_id>/', views.add_comment_reply, name='add_comment_reply'),
    path('exam/<int:moduls_id>/', views.exam_view, name='exam_view'),
    path('exam/submit/', views.exam_submit_view, name='exam_submit_view'),
    path('repeat-exam/<int:moduls_id>/', views.repeat_exam_view, name='repeat_exam'),  # Добавьте этот путь
    path('work_on_mistakes/<int:moduls_id>/', views.work_on_mistakes_view, name='work_on_mistakes'),
]