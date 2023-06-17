from django import forms
from .models import Quiz


class QuizFormAdmin(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = [
            "is_active",
            "title",
            "question_1",
            "answer1_1",
            "answer1_2",
            "answer1_3",
            "answer1_4",
            "correct_answer1",
            "question_2",
            "answer2_1",
            "answer2_2",
            "answer2_3",
            "answer2_4",
            "correct_answer2",
            "question_3",
            "answer3_1",
            "answer3_2",
            "answer3_3",
            "answer3_4",
            "correct_answer3",
            "question_4",
            "answer4_1",
            "answer4_2",
            "answer4_3",
            "answer4_4",
            "correct_answer4",
            "question_5",
            "answer5_1",
            "answer5_2",
            "answer5_3",
            "answer5_4",
            "correct_answer5",
        ]
        widgets = {
            "question1": forms.TextInput(attrs={"class": "form-control"}),
            "question2": forms.TextInput(attrs={"class": "form-control"}),
            "question3": forms.TextInput(attrs={"class": "form-control"}),
            "question4": forms.TextInput(attrs={"class": "form-control"}),
            "question5": forms.TextInput(attrs={"class": "form-control"}),
            "correct_answer1": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "correct_answer2": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "correct_answer3": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "correct_answer4": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "correct_answer5": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "answer1_1": forms.TextInput(attrs={"class": "form-control"}),
            "answer1_2": forms.TextInput(attrs={"class": "form-control"}),
            "answer1_3": forms.TextInput(attrs={"class": "form-control"}),
            "answer1_4": forms.TextInput(attrs={"class": "form-control"}),
            "answer2_1": forms.TextInput(attrs={"class": "form-control"}),
            "answer2_2": forms.TextInput(attrs={"class": "form-control"}),
            "answer2_3": forms.TextInput(attrs={"class": "form-control"}),
            "answer2_4": forms.TextInput(attrs={"class": "form-control"}),
            "answer3_1": forms.TextInput(attrs={"class": "form-control"}),
            "answer3_2": forms.TextInput(attrs={"class": "form-control"}),
            "answer3_3": forms.TextInput(attrs={"class": "form-control"}),
            "answer3_4": forms.TextInput(attrs={"class": "form-control"}),
            "answer4_1": forms.TextInput(attrs={"class": "form-control"}),
            "answer4_2": forms.TextInput(attrs={"class": "form-control"}),
            "answer4_3": forms.TextInput(attrs={"class": "form-control"}),
            "answer4_4": forms.TextInput(attrs={"class": "form-control"}),
            "answer5_1": forms.TextInput(attrs={"class": "form-control"}),
            "answer5_2": forms.TextInput(attrs={"class": "form-control"}),
            "answer5_3": forms.TextInput(attrs={"class": "form-control"}),
            "answer5_4": forms.TextInput(attrs={"class": "form-control"}),
        }


class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = [
            "title",
            "question_1",
            "answer1_1",
            "answer1_2",
            "answer1_3",
            "answer1_4",
            "question_2",
            "answer2_1",
            "answer2_2",
            "answer2_3",
            "answer2_4",
            "question_3",
            "answer3_1",
            "answer3_2",
            "answer3_3",
            "answer3_4",
            "question_4",
            "answer4_1",
            "answer4_2",
            "answer4_3",
            "answer4_4",
            "question_5",
            "answer5_1",
            "answer5_2",
            "answer5_3",
            "answer5_4",
        ]
        widgets = {
            "question1": forms.TextInput(attrs={"class": "form-control"}),
            "question2": forms.TextInput(attrs={"class": "form-control"}),
            "question3": forms.TextInput(attrs={"class": "form-control"}),
            "question4": forms.TextInput(attrs={"class": "form-control"}),
            "question5": forms.TextInput(attrs={"class": "form-control"}),
            "answer1_1": forms.TextInput(attrs={"class": "form-control"}),
            "answer1_2": forms.TextInput(attrs={"class": "form-control"}),
            "answer1_3": forms.TextInput(attrs={"class": "form-control"}),
            "answer1_4": forms.TextInput(attrs={"class": "form-control"}),
            "answer2_1": forms.TextInput(attrs={"class": "form-control"}),
            "answer2_2": forms.TextInput(attrs={"class": "form-control"}),
            "answer2_3": forms.TextInput(attrs={"class": "form-control"}),
            "answer2_4": forms.TextInput(attrs={"class": "form-control"}),
            "answer3_1": forms.TextInput(attrs={"class": "form-control"}),
            "answer3_2": forms.TextInput(attrs={"class": "form-control"}),
            "answer3_3": forms.TextInput(attrs={"class": "form-control"}),
            "answer3_4": forms.TextInput(attrs={"class": "form-control"}),
            "answer4_1": forms.TextInput(attrs={"class": "form-control"}),
            "answer4_2": forms.TextInput(attrs={"class": "form-control"}),
            "answer4_3": forms.TextInput(attrs={"class": "form-control"}),
            "answer4_4": forms.TextInput(attrs={"class": "form-control"}),
            "answer5_1": forms.TextInput(attrs={"class": "form-control"}),
            "answer5_2": forms.TextInput(attrs={"class": "form-control"}),
            "answer5_3": forms.TextInput(attrs={"class": "form-control"}),
            "answer5_4": forms.TextInput(attrs={"class": "form-control"}),
        }
