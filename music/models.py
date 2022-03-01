from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class UserDetails(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    username=models.CharField(max_length=30,unique=True)
    password=models.CharField(max_length=30)

    def __str__(self):
        return f'username:{self.username}'


class SongCategory(models.Model):
    userid=models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    categoryname=models.CharField(max_length=100,unique=True)
    def __str__(self):
        return f'{self.categoryname}'

class Album(models.Model):
    userid=models.ForeignKey(UserDetails,on_delete=models.CASCADE)
    album_name=models.CharField(max_length=50,unique=True)
    artist_name=models.CharField(max_length=50)
    album_logo=models.FileField()
    album_genre=models.ForeignKey(SongCategory,on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.album_name}'

class Song(models.Model):
    album_id=models.ForeignKey(Album,on_delete=models.CASCADE)
    userid=models.ForeignKey(UserDetails,on_delete=models.CASCADE)
    song_name=models.CharField(max_length=50)
    song_image=models.FileField()
    song=models.FileField()
    likes=models.IntegerField(default=0)
    dislikes=models.IntegerField(default=0)

    def __str__(self):
        return f'song_name:{self.song_name}'
    






# class Playlist(models.Model):
    
# class Recent(models.Model):
    
# class Favourite(models.Model):
    
