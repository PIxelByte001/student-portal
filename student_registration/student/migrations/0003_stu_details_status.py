# Generated by Django 5.0.2 on 2024-05-05 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_stu_details_application_filled'),
    ]

    operations = [
        migrations.AddField(
            model_name='stu_details',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
