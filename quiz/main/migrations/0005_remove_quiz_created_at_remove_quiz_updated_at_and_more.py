# Generated by Django 4.2.2 on 2023-06-14 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_quiz_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='quiz',
            name='answer',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='question',
            field=models.CharField(max_length=200),
        ),
    ]
