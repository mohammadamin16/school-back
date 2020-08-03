# Generated by Django 3.0.8 on 2020-07-20 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('T', 'Teacher'), ('S', 'Student')], default='S', max_length=1),
        ),
    ]
