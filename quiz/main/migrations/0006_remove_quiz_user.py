# Generated by Django 4.2.2 on 2023-06-14 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_quiz_created_at_remove_quiz_updated_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='user',
        ),
    ]
