# Generated by Django 3.1.1 on 2020-11-25 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greenBondApp', '0003_auto_20201125_0236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.CharField(blank=True, max_length=10000),
        ),
    ]
