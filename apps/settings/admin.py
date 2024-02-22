from django.contrib import admin
from .models import Settings, Slider, Paket, Teachers, UserProfile
from modeltranslation.admin import TranslationAdmin
from modeltranslation.translator import register, TranslationOptions
# ----------------------------Unregistered Models End---------------------------#
from django.contrib.auth.models import User, Group
admin.site.unregister(Group)
# Register your models here.
# ----------------------------Settings---------------------------#
@register(Settings)
class SettingsTranslationOptions(TranslationOptions):
    fields = ['description']
    hide_default_language = True
@admin.register(Settings)
class SettingsAdmin(TranslationAdmin):
    list_display = ('title', 'description', 'logo', 'email', 'phone')
# ----------------------------Settings End---------------------------#

# ----------------------------Slider---------------------------#
@register(Slider)
class SliderTranslationOptions(TranslationOptions):
    fields = ('title', 'suptitle', 'suptitle2', 'suptitle3')
@admin.register(Slider)
class SliderAdmin(TranslationAdmin):
    list_display = ('title', 'bg_image', 'image', 'suptitle')

# ----------------------------Slider End---------------------------#


# ----------------------------PAKET---------------------------#
@register(Paket)
class PaketTranslationOptions(TranslationOptions):
    fields = ['title']
    required_languages = ('en',)
    hide_default_language = True
@admin.register(Paket)
class PaketAdmin(TranslationAdmin):
    list_display = ('title', 'image', 'ent','price')
    list_display_links = ('title', 'ent')
    prepopulated_fields = {"slug": ("title", )}
# ----------------------------PAKET End---------------------------#


# ----------------------------Teachers---------------------------#
@register(Teachers)
class TeachersTranslationOptions(TranslationOptions):
    fields = ['description']
@admin.register(Teachers)
class TeachersAdmin(TranslationAdmin):
    list_display = ('name', 'image', 'description')
# ----------------------------Teachers End---------------------------#



# @admin.register(Subject)
# class SubjectAdmin(TranslationAdmin):
#     list_display = ['name']
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'school', 'profile_photo')

