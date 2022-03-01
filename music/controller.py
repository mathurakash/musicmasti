from django.urls import path
from . import views
app_name='music'

urlpatterns = [
   path('',views.Index.as_view(),name='home'),
   path('dashboard',views.Home.as_view(),name='dashboard'),
    path('signup/',views.Signupview.as_view(),name='signup'),
    path('login/',views.signin,name='signin'),
    # path('login/',views.Signinview.as_view(),name='signin'),
    path('logout/',views.signout,name='signout'),

    path('add_category/',views.AddCategory.as_view(),name='addcategory'),
    path('category/',views.ViewCategory.as_view(),name='viewcategory'),
    path('category/delete/<int:pk>',views.DelCategory.as_view(),name='delcategory'),
    
    path('my_albums/',views.Myalbum.as_view(),name='myalbum'),
    path('add_album/',views.Addalbum.as_view(),name='addalbum'),
    path('my_albums/update/<int:pk>', views.UpdateAlbum.as_view(),name='updatealbum'),
    path('my_albums/delete/<int:pk>', views.DelAlbum.as_view(),name='deletealbum'),

    path('add_song/',views.Addsong.as_view(),name='addsong'),
    path('my_song/',views.Viewsong.as_view(),name='viewsong'),
    path('my_songs/delete/<int:pk>', views.DelSong.as_view(),name='deletesong'),
    path('my_songs/update_song/<int:pk>', views.UpdateSong.as_view(),name='UpdateSong'),


    path('my_album/view_album_songs/<int:pk>', views.ViewAlbumSongs.as_view(),name='ViewAlbumSongs'),


    path('likesong/<int:pk>',views.SongLike,name='likesong'),
    path('dislikesong/<int:pk>',views.SongDislike,name='dislikesong'),


    path('search',views.Search,name='search'),


]