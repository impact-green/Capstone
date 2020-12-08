# Generated by Django 3.1.1 on 2020-11-25 02:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greenBondApp', '0002_remove_project_prior_spends'),
    ]

    operations = [
        migrations.AddField(
            model_name='bond',
            name='maturity_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='bond',
            name='verifier',
            field=models.CharField(default='', max_length=200),
        ),
    ]