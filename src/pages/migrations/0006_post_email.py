# Generated by Django 3.1.4 on 2022-01-06 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20211223_1939'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='email',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
