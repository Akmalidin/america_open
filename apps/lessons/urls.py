from django.urls import path
from . import views

urlpatterns = [
    path('lesson/<int:lesson_id>/', views.lesson_detail, name='lesson_detail'),
    path('add_comment_reply/<int:lesson_id>/', views.add_comment_reply, name='add_comment_reply'),
]