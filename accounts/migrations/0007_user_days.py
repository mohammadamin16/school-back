# Generated by Django 3.0.8 on 2020-07-20 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0002_day_items'),
        ('accounts', '0006_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='days',
            field=models.ManyToManyField(to='study.Day'),
        ),
    ]