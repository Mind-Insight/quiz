from django import forms
from django.forms import formset_factory
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Quiz


class QuizForm(forms.ModelForm):

    class Meta:
        model = Quiz
        fields = [
            "title",
            "question_1",
            "answer_1",
            "question_2",
            "answer_2",
            "question_3",
            "answer_3",
            "question_4",
            "answer_4",
            "question_5",
            "answer_5",
        ]
