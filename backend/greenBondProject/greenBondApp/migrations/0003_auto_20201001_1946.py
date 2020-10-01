# Generated by Django 3.1.1 on 2020-10-01 19:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greenBondApp', '0002_auto_20200930_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='prior_spends',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='project',
            name='use_of_proceeds',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
