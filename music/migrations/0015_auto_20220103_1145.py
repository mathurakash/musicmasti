# Generated by Django 3.2.6 on 2022-01-03 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0014_auto_20220103_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='song',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
