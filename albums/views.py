from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from playground.models import Song
from .forms import AlbumForm
from .models import Album

@login_required
def album_catalog(request):
    """Display album catalog with optional search."""
    query = request.GET.get('q', '')
    albums = Album.objects.all()

    if query:
        albums = albums.filter(title__icontains=query)  # Search filter

    return render(request, 'albums/albums_catalog.html', {'albums': albums, 'query': query})

@login_required
def album_page(request, album_id):
    """Display a single album and its songs."""
    album = get_object_or_404(Album, id=album_id)
    songs = album.songs.all()  # Get all songs in the album
    return render(request, 'albums/album_page.html', {'album': album, 'songs': songs})

@login_required
def album_form(request):
    """Create a new album."""
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            album = form.save(commit=False)
            album.posted_by = request.user  # Assign uploader
            album.save()
            return redirect('album_catalog')
    else:
        form = AlbumForm()

    return render(request, 'albums/album_form.html', {'form': form})

@login_required
def add_song_to_album(request, song_id, album_id):
    """Assign a song to an album."""
    song = get_object_or_404(Song, id=song_id)
    album = get_object_or_404(Album, id=album_id)

    song.album = album
    song.save()

    return redirect('album_catalog')

@login_required
def remove_song_from_album(request, song_id, album_id):
    """Remove a song from an album."""
    song = get_object_or_404(Song, id=song_id)
    album = get_object_or_404(Album, id=album_id)

    if hasattr(song, 'album') and song.album == album:
        song.album = None  # Unlink song from album
        song.save()

    return redirect('album_page', album_id=album.id)

@login_required
def album_delete(request, album_id):
    """Delete an album."""
    album = get_object_or_404(Album, id=album_id)
    album.delete()

    return redirect('album_catalog')
