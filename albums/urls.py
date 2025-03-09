from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    # Album catalog page
    path('album_catalog/', views.album_catalog, name='album_catalog'),

    # Album details page
    path('album/<int:album_id>/', views.album_page, name='album_page'),
     
    # Create new album
    path('album_form/', views.album_form, name='album_form'),

    # Add song to album
    path('add_song_to_album/<int:song_id>/<int:album_id>/', views.add_song_to_album, name='add_song_to_album'),

    # Remove song from album
    path('remove_song_from_album/<int:song_id>/<int:album_id>/', views.remove_song_from_album, name='remove_song_from_album'),

    # Delete album
    path('delete_album/<int:album_id>/', views.album_delete, name='album_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
