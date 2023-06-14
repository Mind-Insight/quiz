from django.db import models
from django.urls import reverse


class Quiz(models.Model):
    title = models.CharField(max_length=255)
    question_1 = models.CharField(max_length=100)
    answer_1 = models.CharField(max_length=100)
    question_2 = models.CharField(max_length=100)
    answer_2 = models.CharField(max_length=100)
    question_3 = models.CharField(max_length=100)
    answer_3 = models.CharField(max_length=100)
    question_4 = models.CharField(max_length=100)
    answer_4 = models.CharField(max_length=100)
    question_5 = models.CharField(max_length=100)
    answer_5 = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse("main:index")
