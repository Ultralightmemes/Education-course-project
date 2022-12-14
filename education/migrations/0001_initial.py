# Generated by Django 4.1.1 on 2022-09-27 20:32

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('publish_date', models.DateField(default=django.utils.timezone.now, verbose_name='Создан')),
                ('update_date', models.DateField(auto_now=True, verbose_name='Обновлён')),
                ('is_published', models.BooleanField(default=False, verbose_name='Опубликован')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('position', models.PositiveSmallIntegerField(verbose_name='Позиция')),
                ('update_date', models.DateField(auto_now=True, verbose_name='Обновлён')),
                ('text', models.TextField(verbose_name='Текст')),
                ('classname', models.CharField(max_length=255, verbose_name='Тип класса')),
                ('is_published', models.BooleanField(default=False, verbose_name='Опубликован')),
            ],
            options={
                'verbose_name': 'Задание',
                'verbose_name_plural': 'Задания',
                'ordering': ('position',),
            },
        ),
        migrations.CreateModel(
            name='ExerciseTask',
            fields=[
                ('task_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='education.task')),
                ('answer', models.CharField(max_length=255, verbose_name='Ответ')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
            },
            bases=('education.task',),
        ),
        migrations.CreateModel(
            name='TestTask',
            fields=[
                ('task_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='education.task')),
            ],
            options={
                'verbose_name': 'Тест',
                'verbose_name_plural': 'Тесты',
            },
            bases=('education.task',),
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('position', models.PositiveSmallIntegerField(verbose_name='Позиция')),
                ('description', models.TextField(max_length=10000, verbose_name='Описание')),
                ('is_published', models.BooleanField(default=False, verbose_name='Опубликована')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='themes', to='education.course', verbose_name='Курс')),
            ],
            options={
                'verbose_name': 'Тема',
                'verbose_name_plural': 'Темы',
                'ordering': ('position',),
            },
        ),
        migrations.AddField(
            model_name='task',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='education.theme', verbose_name='Тема'),
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('video', models.FileField(blank=True, upload_to='', verbose_name='Видео')),
                ('position', models.PositiveSmallIntegerField(verbose_name='Позиция')),
                ('update_date', models.DateField(auto_now=True, verbose_name='Обновлён')),
                ('text', models.TextField(verbose_name='Текст')),
                ('is_published', models.BooleanField(default=False, verbose_name='Опубликован')),
                ('theme', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lessons', to='education.theme', verbose_name='Тема')),
            ],
            options={
                'verbose_name': 'Урок',
                'verbose_name_plural': 'Уроки',
                'ordering': ('position',),
            },
        ),
        migrations.CreateModel(
            name='CourseCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='education.category')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='education.course')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='courses',
            field=models.ManyToManyField(related_name='categories', through='education.CourseCategories', to='education.course', verbose_name='Курсы'),
        ),
        migrations.CreateModel(
            name='TestOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255, verbose_name='Вариант')),
                ('is_true', models.BooleanField(verbose_name='Правильный')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='education.testtask', verbose_name='Тест')),
            ],
            options={
                'verbose_name': 'Вариант ответа',
                'verbose_name_plural': 'Варианты ответа',
            },
        ),
    ]
