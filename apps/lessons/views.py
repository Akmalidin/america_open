from django.shortcuts import render, redirect, get_object_or_404
from .models import Lesson, Comment, Question, Moduls, UserAnswer
from apps.ent.models import UserAnswerEnt
from django.contrib.auth.decorators import login_required
from .forms import CommentForm, CommentReplyForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from apps.settings.models import Settings
from django.contrib import messages
from django.utils import timezone
from pytz import timezone as pytz_timezone

# Получаем объект для часового пояса 'Asia/Bishkek'
local_tz = pytz_timezone('Asia/Bishkek')

# Получаем текущее локальное время в заданном часовом поясе
local_time = timezone.now().astimezone(local_tz)
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
    user_answers_exist = UserAnswer.objects.filter(user=request.user, question__moduls=moduls).exists()
    # Check if the user has already started the exam
    if request.COOKIES.get('moduls_id') == str(moduls.id) or user_answers_exist:
        # Redirect to my_tests page
        return redirect('my_tests')
    else:

    # Store start time in session
        request.session['start_time'] = local_time.strftime('%d.%m.%Y/%H:%M')

        response = render(request, 'lessons/exam.html', locals())
        response.set_cookie('moduls_id', moduls.id, max_age=3600)
        return response


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
            user_answer = request.POST.get(f'question{question.id}', None)
            if user_answer is not None:  # Check if user_answer is not None
                is_correct = user_answer == question.answer
                UserAnswer.objects.create(
                    question=question,
                    user=request.user,
                    chosen_answer=user_answer,
                    is_correct=is_correct,
                )

        return render(request, 'lessons/result_page.html', context)

    messages.error(request, 'Не удалось сохранить оценку. Пожалуйста, попробуйте ещё раз.')
    return redirect('index')


def repeat_exam_view(request, moduls_id):
    settings = Settings.objects.latest('id')
    moduls = get_object_or_404(Moduls, id=moduls_id)
    questions = Question.objects.filter(moduls=moduls)
    num_questions = len(questions)
    request.session['start_time'] = local_time.strftime('%d.%m.%Y/%H:%M')

    return render(request, 'lessons/repeat_exam.html', locals())
def work_on_mistakes_view(request, moduls_id):
    settings = Settings.objects.latest('id')
    moduls = get_object_or_404(Moduls, id=moduls_id)
    questions = Question.objects.filter(moduls=moduls, is_attempted=True, answer__isnull=False)
    num_questions = len(questions)

    # Очистка сессии от предыдущих результатов теста
    user_answers_exist = UserAnswer.objects.filter(user=request.user, question__moduls=moduls)

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
@login_required
def my_tests(request):
    settings = Settings.objects.latest('id')
    user = request.user
    user_answers = UserAnswer.objects.filter(user=user).select_related('question__moduls')
    user_answers_ent = UserAnswerEnt.objects.filter(user=user).select_related('question__moduls')
    tests = {}
    for answer in user_answers:
        test_id = answer.question.moduls.id
        if test_id not in tests:
            tests[test_id] = {
                'exam': answer.question.moduls,
                'marks': 0,
                'num_questions': 0,
            }
        tests[test_id]['num_questions'] += 1
        if answer.is_correct:
            tests[test_id]['marks'] += 1
    tests_ent = {}
    for answer_ent in user_answers_ent:
        test_id = answer_ent.question.moduls.id
        if test_id not in tests_ent:
            tests_ent[test_id] = {
                'exam': answer_ent.question.moduls,
                'marks': 0,
                'num_questions': 0,
            }
        tests_ent[test_id]['num_questions'] += 1
        if answer_ent.is_correct:
            tests_ent[test_id]['marks'] += 1
    start_time = request.session.get('start_time')
    start_time_ent = request.session.get('start_time_ent')
    return render(request, 'lessons/my_tests.html', locals())
def result_page(request, moduls_id):
    settings = Settings.objects.latest('id')
    moduls = get_object_or_404(Moduls, id=moduls_id)
    questions = Question.objects.filter(moduls=moduls)
    score = request.session.get('score', 0)
    correct_answers = request.session.get('correct_answers', 0)
    incorrect_answers = request.session.get('incorrect_answers', 0)
    user_answers = request.session.get('user_answers', {})
    request.session['correct_answers'] = correct_answers
    request.session['incorrect_answers'] = incorrect_answers
    return render(request, 'lessons/my_tests_result_page.html', locals())
