from django.urls import path

from .views import (
    QuizListView,
    QuizCreateView,
    QuizDetailView,
    quiz_result,
    QuizUpdateView,
    QuizDeleteView,
)


app_name = "main"

urlpatterns = [
    path("", QuizListView.as_view(), name="index"),
    path("create_quiz/", QuizCreateView.as_view(), name="create_quiz"),
    path(
        "quiz_detail/<int:id>/", QuizDetailView.as_view(), name="quiz_detail"
    ),
    path("quiz/result/<int:pk>", quiz_result, name="quiz_result"),
    path("edit_quiz/<int:pk>/", QuizUpdateView.as_view(), name="edit_quiz"),
    path("delete_quiz/<int:pk>", QuizDeleteView.as_view(), name="delete_quiz"),
]
