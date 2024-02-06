from django.shortcuts import render, redirect, get_object_or_404
from .models import Lesson, Comment, Question, Result, Moduls, UserAnswer
from django.contrib.auth.decorators import login_required
from .forms import CommentForm, CommentReplyForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from apps.settings.models import Settings
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
    settings = Settings.objects.latest('id')
    moduls = Moduls.objects.get(id=moduls_id)
    questions = Question.objects.all().filter(moduls=moduls)
    num_questions = len(questions)
    if request.method == 'POST':
        pass
    response= render(request,'lessons/exam.html', locals())
    response.set_cookie('moduls_id',moduls.id)
    return response
from django.http import HttpResponseBadRequest

def exam_submit_view(request):
    settings = Settings.objects.latest('id')
    moduls_list = Moduls.objects.all()
    
    if request.method == 'POST':
        moduls_id = request.COOKIES.get('moduls_id')
        moduls = Moduls.objects.get(id=moduls_id)
        questions = Question.objects.filter(moduls=moduls)
        
        # Проверка, были ли ответы уже сохранены в базе данных
        user_answers_exist = UserAnswer.objects.filter(user=request.user, question__moduls=moduls).exists()
        
        if user_answers_exist:
            # Удалить существующие ответы
            UserAnswer.objects.filter(user=request.user, question__moduls=moduls).delete()

        score = 0
        correct_answers = 0
        incorrect_answers = 0
        user_answers = {}

        for question in questions:
            user_answer = request.POST.get(f'question{question.id}')
            user_answers[question.id] = user_answer

            if user_answer == question.answer:
                score += 1
                correct_answers += 1
            else:
                incorrect_answers += 1

        request.session['score'] = score
        request.session['correct_answers'] = correct_answers
        request.session['incorrect_answers'] = incorrect_answers
        request.session['user_answers'] = user_answers

        context = {
            'score': score,
            'correct_answers': correct_answers,
            'incorrect_answers': incorrect_answers,
            'moduls_id': moduls_id,
            'course_id': moduls.course.id,
            'module_id': moduls.id,
            'user_answers': user_answers,
            'settings': settings,
            'moduls_list': moduls_list,
        }
        user = request.user
        for question in questions:
            user_answer = request.POST.get(f'question{question.id}')
            is_correct = user_answer == question.answer

            UserAnswer.objects.create(
                question=question,
                user=user,
                chosen_answer=user_answer,
                is_correct=is_correct,
            )

        return render(request, 'lessons/result_page.html', context)

    messages.error(request, 'Не удалось сохранить оценку. Пожалуйста, попробуйте ещё раз.')
    return redirect('index')

# def exam_submit_view(request):
#     settings = Settings.objects.latest('id')
#     moduls_list = Moduls.objects.all()
    
#     if request.method == 'POST':
#         moduls_id = request.COOKIES.get('moduls_id')
#         moduls = Moduls.objects.get(id=moduls_id)
#         questions = Question.objects.filter(moduls=moduls)
        

#         score = 0
#         correct_answers = 0
#         incorrect_answers = 0
#         user_answers = {}

#         for question in questions:
#             user_answer = request.POST.get(f'question{question.id}')
#             user_answers[question.id] = user_answer

#             if user_answer == question.answer:
#                 score += 1
#                 correct_answers += 1
#             else:
#                 incorrect_answers += 1

#         request.session['score'] = score
#         request.session['correct_answers'] = correct_answers
#         request.session['incorrect_answers'] = incorrect_answers
#         request.session['user_answers'] = user_answers

#         context = {
#             'score': score,
#             'correct_answers': correct_answers,
#             'incorrect_answers': incorrect_answers,
#             'moduls_id': moduls_id,
#             'course_id': moduls.course.id,
#             'module_id': moduls.id,
#             'user_answers': user_answers,
#             'settings': settings,
#             'moduls_list': moduls_list,
#         }
#         user = request.user
#         for question in questions:
#             user_answer = request.POST.get(f'question{question.id}')
#             is_correct = user_answer == question.answer

#             UserAnswer.objects.create(
#                 question=question,
#                 user=user,
#                 chosen_answer=user_answer,
#                 is_correct=is_correct,
#             )

#         return render(request, 'lessons/result_page.html', context)

#     messages.error(request, 'Не удалось сохранить оценку. Пожалуйста, попробуйте ещё раз.')
#     return redirect('index')




def repeat_exam_view(request, moduls_id):
    settings = Settings.objects.latest('id')
    moduls = get_object_or_404(Moduls, id=moduls_id)
    questions = Question.objects.filter(moduls=moduls)
    num_questions = len(questions)

    return render(request, 'lessons/repeat_exam.html', locals())
def work_on_mistakes_view(request, moduls_id):
    settings = Settings.objects.latest('id')
    moduls = get_object_or_404(Moduls, id=moduls_id)
    questions = Question.objects.filter(moduls=moduls, is_attempted=True, answer__isnull=False)
    num_questions = len(questions)

    # Очистка сессии от предыдущих результатов теста
    request.session.pop('score', None)
    
    request.session.pop('user_answers', None)

    # Получите результаты предыдущего теста
    score = request.session.get('score', 0)
    correct_answers = request.session.get('correct_answers', 0)
    incorrect_answers = request.session.get('incorrect_answers', 0)
    user_answers = request.session.get('user_answers', {})
    request.session['correct_answers'] = correct_answers
    request.session['incorrect_answers'] = incorrect_answers
    # Создайте словарь, содержащий правильные ответы для вопросов
    correct_answers_dict = {q.id: q.answer for q in questions}

    # Получите только вопросы с неправильными ответами
    incorrect_questions = [q for q in questions if user_answers.get(str(q.id), None) != correct_answers_dict.get(q.id)]
    # Создайте словарь с ответами пользователя для каждого вопроса
    user_answers_dict = {q.id: user_answers.get(str(q.id), None) for q in questions}
    return render(request, 'lessons/work_on_mistakes.html', {'settings': settings, 'moduls': moduls, 'questions': questions, 'num_questions': num_questions, 'score': score, 'correct_answers': correct_answers, 'incorrect_answers': incorrect_answers, 'user_answers': user_answers_dict})
