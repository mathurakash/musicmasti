# Generated by Django 3.2.6 on 2021-12-23 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0008_auto_20211222_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.songcategory'),
        ),
    ]