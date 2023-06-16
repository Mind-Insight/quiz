from django import forms
from .models import Quiz


class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        exclude = ("is_active",)


class QuizFormAdmin(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = "__all__"
