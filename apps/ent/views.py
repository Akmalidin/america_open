from .models import Slider, Subjects, QuestionEnt, UserAnswerEnt
from apps.settings.models import Settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest
from apps.settings.models import Settings
from django.contrib import messages

# Create your views here.
def index(request):
    settings = Settings.objects.latest('id')
    slider = Slider.objects.latest("id")
    subjects = Subjects.objects.all()
    return render(request, 'ent.html', locals())

@login_required
def exam_view(request, moduls_id):
    settings = Settings.objects.latest('id')
    moduls = Subjects.objects.get(id=moduls_id)
    questions = QuestionEnt.objects.all().filter(moduls=moduls)
    num_questions = len(questions)
    if request.method == 'POST':
        pass
    response= render(request,'lessons/exam.html', locals())
    response.set_cookie('moduls_id',moduls.id)
    return response

def exam_submit_view(request):
    settings = Settings.objects.latest('id')
    moduls_list = Subjects.objects.all()
    
    if request.method == 'POST':
        moduls_id = request.COOKIES.get('moduls_id')
        moduls = Subjects.objects.get(id=moduls_id)
        questions = QuestionEnt.objects.filter(moduls=moduls)
        
        # Проверка, были ли ответы уже сохранены в базе данных
        user_answers_exist = UserAnswerEnt.objects.filter(user=request.user, question__moduls=moduls).exists()
        
        if user_answers_exist:
            # Удалить существующие ответы
            UserAnswerEnt.objects.filter(user=request.user, question__moduls=moduls).delete()

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
            'course_id': moduls.id,
            'module_id': moduls.id,
            'user_answers': user_answers,
            'settings': settings,
            'moduls_list': moduls_list,
        }
        user = request.user
        for question in questions:
            user_answer = request.POST.get(f'question{question.id}')
            is_correct = user_answer == question.answer

            UserAnswerEnt.objects.create(
                question=question,
                user=user,
                chosen_answer=user_answer,
                is_correct=is_correct,
            )

        return render(request, 'lessons/result_page.html', context)

    messages.error(request, 'Не удалось сохранить оценку. Пожалуйста, попробуйте ещё раз.')
    return redirect('index')




def repeat_exam_view(request, moduls_id):
    settings = Settings.objects.latest('id')
    moduls = get_object_or_404(Subjects, id=moduls_id)
    questions = QuestionEnt.objects.filter(moduls=moduls)
    num_questions = len(questions)

    return render(request, 'lessons/repeat_exam.html', locals())
def work_on_mistakes_view(request, moduls_id):
    settings = Settings.objects.latest('id')
    moduls = get_object_or_404(Subjects, id=moduls_id)
    questions = QuestionEnt.objects.filter(moduls=moduls, is_attempted=True, answer__isnull=False)
    num_questions = len(questions)

    # Получите результаты предыдущего теста
    score = request.session.get('score', 0)
    correct_answers = request.session.get('correct_answers', 0)
    incorrect_answers = request.session.get('incorrect_answers', 0)
    user_answers = request.session.get('user_answers', {})

    # Создайте словарь, содержащий правильные ответы для вопросов
    correct_answers_dict = {q.id: q.answer for q in questions}

    # Получите только вопросы с неправильными ответами
    incorrect_questions = [q for q in questions if user_answers.get(str(q.id), None) != correct_answers_dict.get(q.id)]
    # Создайте словарь с ответами пользователя для каждого вопроса
    user_answers_dict = {q.id: user_answers.get(str(q.id), None) for q in questions}
    return render(request, 'lessons/work_on_mistakes.html', {'settings': settings, 'moduls': moduls, 'questions': questions, 'num_questions': num_questions, 'score': score, 'correct_answers': correct_answers, 'incorrect_answers': incorrect_answers, 'user_answers': user_answers_dict})