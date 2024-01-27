from django.shortcuts import render, redirect, get_object_or_404
from .models import Lesson, Comment, Question, Result, Moduls
from django.contrib.auth.decorators import login_required
from .forms import CommentForm, CommentReplyForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from apps.settings.models import Settings
from apps.courses.models import Courses
from django.contrib import messages

def lesson_detail(request, lesson_id):
    settings = Settings.objects.latest('id')
    lesson = get_object_or_404(Lesson, id=lesson_id)
    module = lesson.module
    course = module.course
    comments = Comment.objects.filter(lesson=lesson)
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        reply_form = CommentReplyForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.lesson = lesson
            comment.save()
            return redirect('lesson_detail', lesson_id=lesson_id)

        elif reply_form.is_valid():
            reply = reply_form.save(commit=False)
            reply.user = request.user
            reply.comment = Comment.objects.get(pk=request.POST.get('comment_id'))
            reply.save()
            return redirect('lesson_detail', lesson_id=lesson_id)
    else:
        comment_form = CommentForm()
        reply_form = CommentReplyForm()

    return render(request, 'lessons/lesson_detail.html', locals())

def add_comment_reply(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)

    if request.method == 'POST':
        reply_form = CommentReplyForm(request.POST)
        if reply_form.is_valid():
            reply = reply_form.save(commit=False)
            reply.user = request.user
            reply.lesson = lesson  
            reply.comment = Comment.objects.get(pk=request.POST.get('comment_id'))
            reply.save()
            return HttpResponseRedirect(reverse('lesson_detail', args=[lesson_id]))

    return HttpResponseRedirect(reverse('lesson_detail', args=[lesson_id]))

@login_required
def exam_view(request, moduls_id):
    moduls = Moduls.objects.get(id=moduls_id)
    questions = Question.objects.all().filter(moduls=moduls)
    num_questions = len(questions)
    if request.method == 'POST':
        pass
    response= render(request,'lessons/exam.html', locals())
    response.set_cookie('moduls_id',moduls.id)
    return response
def exam_submit_view(request):
    if request.method == 'POST':
        moduls_id = request.COOKIES.get('moduls_id')
        moduls = Moduls.objects.get(id=moduls_id)
        questions = Question.objects.filter(moduls=moduls)
        
        score = 0
        
        for question in questions:
            user_answer = request.POST.get(f'question{question.id}')
            if user_answer == question.answer:
                score += 1
        
        messages.success(request, f'Ваша оценка: {score}/{len(questions)}')

        return redirect('result_page')

    messages.error(request, 'Не удалось сохранить оценку. Пожалуйста, попробуйте ещё раз.')
    return redirect('index')

def result_page(request):
    settings = Settings.objects.latest('id')
    return render(request, 'lessons/result_page.html', locals())