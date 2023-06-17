from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


User = get_user_model()


class Quiz(models.Model):
    is_active = models.BooleanField(default=True)
    title = models.CharField(max_length=255, verbose_name="Название")
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="quizzes",
        null=True,
    )
    score = models.IntegerField(default=0)
    question_1 = models.CharField(max_length=255, verbose_name="Вопрос1")
    answer1_1 = models.CharField(max_length=255, verbose_name="Ответ 1_1")
    answer1_2 = models.CharField(max_length=255, verbose_name="Ответ 1_2")
    answer1_3 = models.CharField(max_length=255, verbose_name="Ответ 1_3")
    answer1_4 = models.CharField(max_length=255, verbose_name="Ответ 1_4")
    correct_answer1 = models.CharField(
        max_length=255, verbose_name="Правильный ответ 1"
    )
    question_2 = models.CharField(max_length=255, verbose_name="Вопрос 2")
    answer2_1 = models.CharField(max_length=255, verbose_name="Ответ 2_1")
    answer2_2 = models.CharField(max_length=255, verbose_name="Ответ 2_2")
    answer2_3 = models.CharField(max_length=255, verbose_name="Ответ 2_3")
    answer2_4 = models.CharField(max_length=255, verbose_name="Ответ 2_4")
    correct_answer2 = models.CharField(
        max_length=255, verbose_name="Правильный ответ 2"
    )
    question_3 = models.CharField(max_length=255, verbose_name="Вопрос 3")
    answer3_1 = models.CharField(max_length=255, verbose_name="Ответ 3_1")
    answer3_2 = models.CharField(max_length=255, verbose_name="Ответ 3_2")
    answer3_3 = models.CharField(max_length=255, verbose_name="Ответ 3_3")
    answer3_4 = models.CharField(max_length=255, verbose_name="Ответ 3_4")
    correct_answer3 = models.CharField(
        max_length=255, verbose_name="Правильный ответ 3"
    )
    question_4 = models.CharField(max_length=255, verbose_name="Вопрос 4")
    answer4_1 = models.CharField(max_length=255, verbose_name="Ответ 4_1")
    answer4_2 = models.CharField(max_length=255, verbose_name="Ответ 4_2")
    answer4_3 = models.CharField(max_length=255, verbose_name="Ответ 4_3")
    answer4_4 = models.CharField(max_length=255, verbose_name="Ответ 4_4")
    correct_answer4 = models.CharField(
        max_length=255, verbose_name="Правильный ответ 4"
    )
    question_5 = models.CharField(max_length=255, verbose_name="Вопрос 5")
    answer5_1 = models.CharField(max_length=255, verbose_name="Ответ 5_1")
    answer5_2 = models.CharField(max_length=255, verbose_name="Ответ 5_2")
    answer5_3 = models.CharField(max_length=255, verbose_name="Ответ 5_3")
    answer5_4 = models.CharField(max_length=255, verbose_name="Ответ 5_4")
    correct_answer5 = models.CharField(
        max_length=255, verbose_name="Правильный ответ 5"
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("main:index")
