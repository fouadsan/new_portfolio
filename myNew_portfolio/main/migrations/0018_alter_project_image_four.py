# Generated by Django 3.2.4 on 2021-07-05 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20210705_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image_four',
            field=models.ImageField(blank=True, upload_to='projects'),
        ),
    ]
