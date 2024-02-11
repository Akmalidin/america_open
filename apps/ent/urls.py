from django.urls import path
from .views import index, exam_view, exam_submit_view, repeat_exam_view, work_on_mistakes_view

urlpatterns = [
    path('', index, name='ent'),
    path('exam/<int:moduls_id>/', exam_view, name='exam_view_ent'),
    path('exam_ent/submit/', exam_submit_view, name='exam_submit_view_ent'),
    path('repeat-exam_ent/<int:moduls_id>/', repeat_exam_view, name='repeat_exam_ent'),  
    path('work_on_mistakes_ent/<int:moduls_id>/', work_on_mistakes_view, name='work_on_mistakes_ent'),
]
