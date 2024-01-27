from django.urls import path
from . import views

urlpatterns = [
    path('lesson/<int:lesson_id>/', views.lesson_detail, name='lesson_detail'),
    path('add_comment_reply/<int:lesson_id>/', views.add_comment_reply, name='add_comment_reply'),
    path('exam/<int:moduls_id>/', views.exam_view, name='exam_view'),
    path('exam/submit/', views.exam_submit_view, name='exam_submit_view'),
    path('result/', views.result_page, name='result_page'),
]