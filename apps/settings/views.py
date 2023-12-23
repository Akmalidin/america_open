from django.shortcuts import render, redirect
from .models import Settings, Slider, Paket, Teachers, UserProfile
# Create your views here.
def index(request):
    settings = Settings.objects.latest("id")
    slider = Slider.objects.all()
    paket = Paket.objects.all()
    teachers = Teachers.objects.all()
    return render(request, 'index.html', locals())





