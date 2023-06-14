from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView

from .forms import QuizForm
from .models import Quiz


class QuizListView(LoginRequiredMixin, ListView):
    model = Quiz
    ordering = "id"
    paginate_by = 5
    queryset = Quiz.objects.all()
    context_object_name = "quizzes"
    template_name = "main/index.html"


class QuizCreateView(LoginRequiredMixin, CreateView):
    model = Quiz
    form_class = QuizForm
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
    correct_answer = 0
    quiz = Quiz.objects.get(pk=pk)
    user_answers = list(request.POST.dict().values())
    if quiz.answer_1 == user_answers[1]:
        correct_answer += 1
    if quiz.answer_2 == user_answers[2]:
        correct_answer += 1
    if quiz.answer_3 == user_answers[3]:
        correct_answer += 1
    if quiz.answer_4 == user_answers[4]:
        correct_answer += 1
    if quiz.answer_5 == user_answers[5]:
        correct_answer += 1
    return render(
        request,
        "main/quiz_result.html",
        {"correct_answers": correct_answer},
    )
