# Generated by Django 4.1.1 on 2022-09-28 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0003_alter_task_lesson'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='courses',
            field=models.ManyToManyField(blank=True, related_name='categories', through='education.CourseCategories', to='education.course', verbose_name='Курсы'),
        ),
        migrations.AlterField(
            model_name='task',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='education.lesson', verbose_name='Урок'),
        ),
    ]
