from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from .models import UserDetails,SongCategory,Album,Song
from django.urls import reverse_lazy
from .myforms import Signinform, Signupform
from django.http import HttpResponseRedirect

# Create your views here.
class Index(ListView):
    template_name="music/index.html"
    context_object_name="form"
    def get_queryset(self):
        return{'alb':Album.objects.all(),'songs':Song.objects.all()}



def SongLike(request,pk):
    song = Song.objects.get(id=pk)
    song.likes += 1
    song.save()
    return redirect('music:home')

def SongDislike(request,pk):
    song = Song.objects.get(id=pk)
    song.dislikes += 1
    song.save()
    return redirect('music:home')




def Search(request):
    if request.method == "POST":
        name = request.POST.get('Searchbar')
        print (name)
        albums=Album.objects.filter(album_name__contains=name)
        songs=Song.objects.filter(song_name__contains=name)
        print(albums)
        return render(request,'music/Search.html',{'name':name,'album':albums,"song":songs})
    else:
        return render(request,'music/Search.html')








# class Search(ListView):
#     template_name="music/Search.html"
#     context_object_name="form"
#     def get_queryset(self,search):
#         if search.method == "POST":
#             name = search.POST.get('Searchbar')
#             return {'name':name}
#         else:
#             return None





class Home(ListView):
    template_name="music/dashboard.html"
    context_object_name="form"
    def get_queryset(self):
        u=self.request.session.get('user_log')
        alb1=UserDetails.objects.get(username=u.get('username'))
        ccount=SongCategory.objects.filter(userid=alb1).count()
        acount=Album.objects.filter(userid=alb1).count()
        scount=Song.objects.filter(userid=alb1).count()
        print(ccount,acount,scount)
        return {'cat':ccount,'album':acount,'song':scount}

        

class ViewAlbumSongs(ListView):
    template_name="music/album_songs.html"
    context_object_name="form"
    def get_queryset(self):
        albumid=self.kwargs.get('pk')
        album=Album.objects.get(id=albumid)
        return {'albumname':album.album_name, 'song':album.song_set.all()}


# class Home(ListView):
#     template_name='music/index.html'
#     context_object_name='form'
#     model=Song
#     def get_queryset(self):
#         u=self.request.session.get("user_log")
#         if u:
#             alb1=UserDetails.objects.get(username=u.get('username'))
#             return {'alb':Song.objects.all()}
#         else:
#             return None


class Signupview(CreateView):
    template_name='music/signup.html'
    context_object_name='form'
    model=UserDetails
    form_class=Signupform
    success_url=reverse_lazy('music:signin')
    def form_valid(self, form):
        tempform=form.save(commit=False)
        p=form.cleaned_data['password']
        tempform.password=make_password(p)
        tempform.save()
        return super().form_valid(form)

    
def signin(request):
    f=Signinform(request.POST or None)
    if f.is_valid():
        u=f.cleaned_data.get('username')
        obj=UserDetails.objects.get(username=u)
        request.session['user_log']={'username':obj.username}
        return redirect('music:dashboard')
    return render(request,'music/signin.html',{'form':f})


def signout(request):
    request.session.pop("user_log")
    return redirect("music:home")


class AddCategory(CreateView):
    template_name='music/add_category.html'
    model=SongCategory
    fields=['categoryname']
    context_object_name='form'
    success_url=reverse_lazy('music:home')
    def form_valid(self,form):
        u=self.request.session.get('user_log')
        u1=UserDetails.objects.get(username=u.get('username'))
        form.instance.userid=u1        
        return super().form_valid(form)

class DelCategory(DeleteView):
    template_name='music/delcat.html'
    model=SongCategory
    context_object_name='form'
    success_url=reverse_lazy('music:viewcategory')
    success_message='product deleted'

class ViewCategory(ListView):
    template_name='music/view_category.html'
    context_object_name='form'
    model=SongCategory
    def get_queryset(self):
        u=self.request.session.get("user_log")
        if u:
            alb1=UserDetails.objects.get(username=u.get('username'))
            return {'alb':SongCategory.objects.filter(userid=alb1)}
        else:
            return None


class AddCategory(CreateView):
    template_name='music/add_category.html'
    model=SongCategory
    fields=['categoryname']
    context_object_name='form'
    success_url=reverse_lazy('music:viewcategory')
    def form_valid(self,form):
        u=self.request.session.get('user_log')
        u1=UserDetails.objects.get(username=u.get('username'))
        form.instance.userid=u1        
        return super().form_valid(form)



class Addalbum(CreateView):
    model=Album
    template_name='music/add_album.html'
    success_url=reverse_lazy('music:addsong')
    fields=['album_name','artist_name','album_logo','album_genre']
    context_object_name='form'
    def form_valid(self,form):
        u=self.request.session.get('user_log')
        u1=UserDetails.objects.get(username=u.get('username'))
        form.instance.userid=u1
        return super().form_valid(form)

class UpdateAlbum(UpdateView):
    template_name='music/add_album.html'
    model=Album
    fields=['album_name','artist_name','album_logo','album_genre']
    context_object_name='form'
    success_url=reverse_lazy('music:myalbum')

class DelAlbum(DeleteView):
    template_name='music/delalbum.html'
    model=Album
    context_object_name='form'
    success_url=reverse_lazy('music:myalbum')
    success_message='product deleted'

class Myalbum(ListView):
    template_name='music/view_album.html'
    context_object_name='form'
    model=Album
    def get_queryset(self):
        u=self.request.session.get("user_log")
        if u:
            alb1=UserDetails.objects.get(username=u.get('username'))
            return {'alb':Album.objects.filter(userid=alb1)}
        else:
            return None



class Addsong(CreateView):
    model=Song
    template_name='music/add_song.html'
    success_url=reverse_lazy('music:viewsong')
    fields=['album_id','song_name','song_image','song']
    context_object_name='form'
    def form_valid(self,form):
        u=self.request.session.get('user_log')
        u1=UserDetails.objects.get(username=u.get('username'))
        form.instance.userid=u1
        return super().form_valid(form)

class DelSong(DeleteView):
    template_name='music/delsong.html'
    model=Song
    context_object_name='form'
    success_url=reverse_lazy('music:viewsong')
    success_message='Song deleted'


class Viewsong(ListView):
    template_name='music/view_songs.html'
    context_object_name='form'
    model=Song
    def get_queryset(self):
        u=self.request.session.get("user_log")
        if u:
            alb1=UserDetails.objects.get(username=u.get('username'))
            return {'alb':Song.objects.filter(userid=alb1)}
        else:
            return None

class UpdateSong(UpdateView):
    template_name='music/add_song.html'
    model=Song
    fields=['album_id','song_name','song_image','song']
    context_object_name='form'
    success_url=reverse_lazy('music:viewsong')