# Generated by Django 4.2.2 on 2023-06-14 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_quiz_answer_quiz_question_alter_quiz_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='description',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='title',
        ),
    ]
