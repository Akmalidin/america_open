from django import forms
from .models import Comment, Homework

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

class HomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework
        fields = ('file',)