# Generated by Django 3.2.16 on 2023-06-16 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_quiz_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='correct_answer1',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='correct_answer2',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='correct_answer3',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='correct_answer4',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='correct_answer5',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
