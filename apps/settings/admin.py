from django.contrib import admin

from .models import Settings, Slider, Paket, Teachers, UserProfile
# Register your models here.
@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'logo', 'email', 'phone')
@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'bg_image', 'image', 'suptitle')
@admin.register(Paket)
class PaketAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'ent')
@admin.register(Teachers)
class TeachersAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'description')
# @admin.register(Subject)
# class SubjectAdmin(admin.ModelAdmin):
#     list_display = ['name']
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'school', 'profile_photo')