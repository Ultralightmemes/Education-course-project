# Generated by Django 4.1.1 on 2022-10-06 08:26

from django.db import migrations, models
import education.models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0009_alter_course_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='video',
            field=models.FileField(blank=True, upload_to='lesson/%Y/%m/%d', validators=[education.models.validate_file_extension], verbose_name='Видео'),
        ),
    ]
