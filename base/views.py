from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Playlist
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView


# Create your views here.

class Songslist(ListView):
    model= Playlist
    context_object_name= "playlists"
    template_name = "base/Song_list.html"

class UserSongslist(ListView):
    model = Playlist
    context_object_name= "user_playlists"
    template_name = "base/usersongs_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_playlists'] = context['user_playlists'].filter(user=self.request.user)
        context['count'] = context['user_playlists'].count()
        return context

class PlaylistDetails(DetailView):
    model = Playlist
    context_object_name = "playlists"

class CreatePlaylist(CreateView):
    model=Playlist
    fields = "__all__"
    success_url = reverse_lazy("posted_playlist")

class UpdatePlaylist(UpdateView):
    model = Playlist
    fields = "__all__"
    success_url = reverse_lazy("posted_playlist")

class DeletePlaylist(DeleteView):
    model=Playlist
    context_object_name = "playlists"
    success_url = reverse_lazy("posted_playlist")