from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    #Saved songs catalog
    path('saved_songs/', views.saved_songs_catalog, name='saved_songs'),

    #Save song
    path('saved_song/<int:song_id>/', views.song_save, name='song_save'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)