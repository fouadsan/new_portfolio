# Generated by Django 3.2.4 on 2021-07-05 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20210705_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(upload_to='profile_pics'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image_one',
            field=models.ImageField(upload_to='projects'),
        ),
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(upload_to='services'),
        ),
    ]
