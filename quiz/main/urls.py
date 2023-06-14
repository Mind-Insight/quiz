from django.urls import path

from .views import QuizListView, QuizCreateView, QuizDetailView, quiz_result


app_name = 'main'

urlpatterns = [
    path("", QuizListView.as_view(), name="index"),
    path("create_quiz/", QuizCreateView.as_view(), name='create_quiz'),
    path("quiz_detail/<int:id>/", QuizDetailView.as_view(), name="quiz_detail"),
    path('quiz/result/<int:pk>', quiz_result, name='quiz_result'),
]
