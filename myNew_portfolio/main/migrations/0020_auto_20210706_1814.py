# Generated by Django 3.2.4 on 2021-07-06 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20210706_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='social',
            name='my_facebook',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='social',
            name='my_linkedin',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='social',
            name='my_twitter',
            field=models.URLField(),
        ),
    ]
