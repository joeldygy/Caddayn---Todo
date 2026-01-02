from django.urls import path
from core_app.song.controller import SongController

urlpatterns = [
    path('', SongController.get_all, name='song_list'),
    path('create/', SongController.create, name='song_create'),
    path('<int:id>/', SongController.get, name='song_detail'),
    path('<int:id>/update/', SongController.update, name='song_update'),
    path('<int:id>/delete/', SongController.delete, name='song_delete'),
]
