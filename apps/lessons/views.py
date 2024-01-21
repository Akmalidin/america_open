from django.shortcuts import render, redirect, get_object_or_404
from .models import Lesson, Comment
from .forms import CommentForm, CommentReplyForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from apps.settings.models import Settings
from apps.courses.models import Courses

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

    # return render(request, 'lessons/lesson_detail.html', locals())
    # lesson = get_object_or_404(Lesson, id=lesson_id)

    # if request.method == 'POST':
    #     form = CommentForm(request.POST)
    #     if form.is_valid():
    #         comment = form.save(commit=False)
    #         comment.user = request.user
    #         comment.lesson = lesson
    #         comment.save()
    #         return redirect('lesson_detail', lesson_id=lesson_id)
    # else:
    #     form = CommentForm()

    # return render(request, 'add_comment.html', locals())

def add_comment_reply(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)

    if request.method == 'POST':
        reply_form = CommentReplyForm(request.POST)
        if reply_form.is_valid():
            reply = reply_form.save(commit=False)
            reply.user = request.user
            reply.lesson = lesson  # Set the lesson for the reply
            reply.comment = Comment.objects.get(pk=request.POST.get('comment_id'))
            reply.save()
            return HttpResponseRedirect(reverse('lesson_detail', args=[lesson_id]))

    # Redirect back to the lesson detail page if the form is not valid
    return HttpResponseRedirect(reverse('lesson_detail', args=[lesson_id]))