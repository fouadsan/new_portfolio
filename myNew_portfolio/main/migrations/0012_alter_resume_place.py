# Generated by Django 3.2.4 on 2021-07-03 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_skill_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='place',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]