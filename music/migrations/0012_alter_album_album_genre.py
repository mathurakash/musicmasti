# Generated by Django 3.2.6 on 2021-12-23 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0011_alter_album_album_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_genre',
            field=models.CharField(max_length=50),
        ),
    ]
