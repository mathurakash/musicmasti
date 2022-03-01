from django.contrib import admin
from .models import UserDetails,SongCategory,Album,Song


# Register your models here.
admin.site.register(UserDetails)
admin.site.register(SongCategory)
admin.site.register(Album)
admin.site.register(Song)