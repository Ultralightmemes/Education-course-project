# Generated by Django 4.1.1 on 2022-11-22 11:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_userlesson_is_done'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercourse',
            name='rating',
            field=models.IntegerField(default=None, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
