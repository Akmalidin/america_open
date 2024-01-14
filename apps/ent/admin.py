from django.contrib import admin
from .models import Slider, Subjects
# Register your models here.
@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'bg_image', 'image', 'description')
@admin.register(Subjects)
class SubjectsAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'btn')