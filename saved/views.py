from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile, SavedSong
from playground.models import Song

@login_required
def saved_songs_catalog(request):
    """Catalog of saved songs"""
    query = request.GET.get('q', '')

    profile, _ = UserProfile.objects.get_or_create(user=request.user)
    saved_songs = profile.saved_songs.all()

    if query:
        saved_songs = saved_songs.filter(title__icontains=query)

    return render(request, 'saved/saved_songs_catalog.html', {'saved_songs': saved_songs, 'query': query})

@login_required
def song_save(request, song_id):
    """Function for save song"""
    song = get_object_or_404(Song, id=song_id)
    profile, _ = UserProfile.objects.get_or_create(user=request.user)

    saved_song, created = SavedSong.objects.get_or_create(
        original_song = song,
        user_profile = profile,
        defaults={
            'title': song.title,
            'video': song.video,
            'cover_image': song.cover_image,
            'audio': song.audio,
            'author': song.author,
            'posted_by': song.posted_by,
        }
    )

    if not created:
        saved_song.delete()

    return redirect('saved_songs')

