from django.urls import path
from .views import Songslist,PlaylistDetails,CreatePlaylist,UserSongslist,UpdatePlaylist,DeletePlaylist

urlpatterns=[
    path("",Songslist.as_view(),name="home"),
    path("playlist-detail/<int:pk>/",PlaylistDetails.as_view(),name="playlist_details"),
    path("playlist-create/",CreatePlaylist.as_view(), name="playlist_create"),
    path("posted-playlist/",UserSongslist.as_view() , name="posted_playlist"),
    path("playlist-update/<int:pk>/",UpdatePlaylist.as_view(),name="playlist_update"),
    path("playlist-delete/<int:pk>/",DeletePlaylist.as_view(), name="playlist_delete")
]