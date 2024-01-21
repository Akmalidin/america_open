from django.shortcuts import render
from .models import Slider, Subjects
from apps.settings.models import Settings
# Create your views here.
def index(request):
    settings = Settings.objects.latest('id')
    slider = Slider.objects.latest("id")
    subjects = Subjects.objects.all()
    return render(request, 'ent.html', locals())

def test(request):
    return render(request, 'tests/test.html', locals())