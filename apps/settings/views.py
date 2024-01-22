from django.shortcuts import render, redirect, get_object_or_404
from .models import Settings, Slider, Paket, Teachers, UserProfile
# Create your views here.
def index(request):
    settings = Settings.objects.latest("id")
    slider = Slider.objects.all()
    paket = Paket.objects.all()
    teachers = Teachers.objects.all()
    return render(request, 'index.html', locals())

def packet(request, slug):
    paket = get_object_or_404(Paket, slug=slug)
    settings = Settings.objects.latest('id')
    return render(request, 'packages.html', locals())

# def choose_paket(request):
#     # Получение списка тарифов
#     pakets = Paket.objects.all()

#     if request.method == 'POST':
#         # Обработка выбора тарифа
#         paket_slug = request.POST.get('selected_paket_slug')
#         selected_paket = Paket.objects.get(slug=paket_slug)

#         # Сохранение выбранного тарифа в профиле пользователя
#         user_profile, created = UserProfile.objects.get_or_create(user=request.user)
#         user_profile.selected_paket = selected_paket
#         user_profile.save()

#     # Получение профиля пользователя (если он существует)
#     user_profile = UserProfile.objects.filter(user=request.user).first()

#     # Передача списка тарифов и выбранного тарифа в контекст шаблона
#     return render(request, 'choose_paket.html', locals())
