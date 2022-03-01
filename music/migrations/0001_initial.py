# Generated by Django 3.2.6 on 2021-12-21 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=50)),
                ('artist_name', models.CharField(max_length=50)),
                ('album_logo', models.FileField(upload_to='')),
                ('album_genre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='SongCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryname', models.CharField(max_length=100)),
                ('uid', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='music.userdetails')),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_name', models.CharField(max_length=50)),
                ('song_image', models.FileField(upload_to='')),
                ('song', models.FileField(upload_to='')),
                ('album_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.album')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='userid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.userdetails'),
        ),
    ]
