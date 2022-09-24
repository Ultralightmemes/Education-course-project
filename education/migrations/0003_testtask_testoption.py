# Generated by Django 4.1.1 on 2022-09-23 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0002_alter_lesson_options_alter_theme_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestTask',
            fields=[
                ('lesson_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='education.lesson')),
            ],
            options={
                'verbose_name': 'Тест',
                'verbose_name_plural': 'Тесты',
            },
            bases=('education.lesson',),
        ),
        migrations.CreateModel(
            name='TestOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255, verbose_name='Вариант')),
                ('is_true', models.BooleanField(verbose_name='Правильный')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='education.testtask', verbose_name='Тест')),
            ],
            options={
                'verbose_name': 'Вариант ответа',
                'verbose_name_plural': 'Варианты ответа',
            },
        ),
    ]