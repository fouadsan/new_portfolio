# Generated by Django 3.2.4 on 2021-07-03 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_rename_name_resume_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='date',
            field=models.DateField(),
        ),
    ]