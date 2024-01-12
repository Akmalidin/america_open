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


