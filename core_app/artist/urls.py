from django.urls import path

from core_app.artist.controller import ArtistController

urlpatterns = [
    path('', ArtistController.get_all, name='artist_list'),
    path('create/', ArtistController.create, name='artist_create'),
    path('<int:id>/', ArtistController.get, name='artist_detail'),
    path('<int:id>/update/', ArtistController.update, name='artist_update'),
    path('<int:id>/delete/', ArtistController.delete, name='artist_delete'),
]
