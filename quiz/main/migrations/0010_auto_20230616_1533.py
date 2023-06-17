# Generated by Django 3.2.16 on 2023-06-16 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20230616_0607'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='answer_1',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='answer_2',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='answer_3',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='answer_4',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='answer_5',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='is_active',
        ),
        migrations.AddField(
            model_name='quiz',
            name='answer1_1',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='answer1_2',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='answer1_3',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='answer1_4',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='answer2_1',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='answer2_2',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='answer2_3',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='answer2_4',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='answer3_1',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='answer3_2',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='answer3_3',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='answer3_4',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='answer4_1',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='answer4_2',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='answer4_3',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='answer4_4',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='answer5_1',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='answer5_2',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='answer5_3',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='answer5_4',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='quiz',
            name='question_1',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='question_2',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='question_3',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='question_4',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='question_5',
            field=models.CharField(max_length=255),
        ),
    ]
