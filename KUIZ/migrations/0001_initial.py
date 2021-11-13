# Generated by Django 3.2.7 on 2021-11-13 06:41

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('point', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz_topic', models.CharField(max_length=200)),
                ('detail', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published')),
                ('end_date', models.DateTimeField(default=datetime.datetime(2021, 11, 14, 6, 41, 51, 392979, tzinfo=utc), verbose_name='date end')),
                ('topic', models.CharField(choices=[('', '----------'), ('programming', 'Programming'), ('mathematics', 'Mathematics'), ('physics', 'Physics'), ('chemistry', 'Chemistry'), ('biology', 'Biology'), ('astronomy', 'Astronomy'), ('social', 'Social'), ('sport', 'Sport'), ('others', 'Others')], default='others', max_length=20)),
                ('exam_duration', models.IntegerField(default=0)),
                ('score', models.IntegerField(default=0)),
                ('random_order', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default='No')),
                ('automate', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default='Yes')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(default='', max_length=200)),
                ('correct', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='KUIZ.question')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='KUIZ.quiz'),
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_text', models.TextField(max_length=5000)),
                ('quiz', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='KUIZ.quiz')),
                ('user', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('correct', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='KUIZ.question')),
            ],
        ),
    ]
