# Generated by Django 5.0.2 on 2024-05-05 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stu_details',
            name='application_filled',
            field=models.BooleanField(default=False),
        ),
    ]
