from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)

from .forms import QuizFormAdmin
from .models import Quiz


class QuizListView(LoginRequiredMixin, ListView):
    model = Quiz
    ordering = "id"
    paginate_by = 5
    context_object_name = "quizzes"
    template_name = "main/index.html"

    def get_queryset(self):
        if self.request.user.is_superuser:
            queryset = Quiz.objects.all()
        else:
            queryset = Quiz.objects.filter(is_active=True)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pass_users"] = Quiz.objects.filter(score=5).count()
        return context


class QuizDeleteView(LoginRequiredMixin, DeleteView):
    model = Quiz
    template_name = "main/confirm_delete.html"
    success_url = reverse_lazy("main:index")


class QuizUpdateView(LoginRequiredMixin, UpdateView):
    model = Quiz
    form_class = QuizFormAdmin
    template_name = "main/edit_quiz.html"


class QuizCreateView(LoginRequiredMixin, CreateView):
    model = Quiz
    form_class = QuizFormAdmin
    template_name = "main/create_quiz.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("main:index")


class QuizDetailView(LoginRequiredMixin, DetailView):
    model = Quiz
    template_name = "main/quiz_detail.html"
    context_object_name = "quiz"

    def get_object(self, query_set=None):
        id = self.kwargs.get("id")
        return Quiz.objects.get(id=id)


def quiz_result(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    answers = []
    score = 0
    correct = []
    for i in range(1, 6):
        answer = request.POST.get(f"question_{i}")
        answers.append(answer)
    if not answers:
        score = 0
    else:
        correct.append(quiz.correct_answer1)
        correct.append(quiz.correct_answer2)
        correct.append(quiz.correct_answer3)
        correct.append(quiz.correct_answer4)
        correct.append(quiz.correct_answer5)
        if quiz.correct_answer1 == answers[0]:
            score += 1
        if quiz.correct_answer2 == answers[1]:
            score += 1
        if quiz.correct_answer3 == answers[2]:
            score += 1
        if quiz.correct_answer4 == answers[3]:
            score += 1
        if quiz.correct_answer5 == answers[4]:
            score += 1

    quiz.score = score
    quiz.save()
    return render(
        request,
        "main/quiz_result.html",
        {
            "correct_answers": score,
            "answers": correct,
        },
    )
