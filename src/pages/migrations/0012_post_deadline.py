# Generated by Django 3.2.9 on 2022-01-20 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_auto_20220119_2253'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='deadline',
            field=models.DateField(null=True),
        ),
    ]
