from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from saved.models import UserProfile
from albums.models import Album
from .forms import SongForm
from .models import Song

@login_required
def song_catalog(request):
    """Song catalog"""
    query = request.GET.get('q', '')  # Get search query
    songs = Song.objects.all()

    saved_songs = []
    if request.user.is_authenticated:
        profile = get_object_or_404(UserProfile, user=request.user)
        saved_songs = profile.saved_songs.values_list('original_song_id', flat=True)

    if query:
        songs = songs.filter(title__icontains=query)  # Filter songs by title

    return render(request, 'playground/song_catalog.html', {'songs': songs, 'saved_songs': saved_songs, 'query': query})

@login_required
def song_page(request, song_id):
    """Song page"""
    song = get_object_or_404(Song, id=song_id)
    albums = Album.objects.all()  # Get all albums

    saved_songs = []
    if request.user.is_authenticated:
        profile = get_object_or_404(UserProfile, user=request.user)
        saved_songs = profile.saved_songs.values_list('original_song_id', flat=True)

    return render(request, 'playground/song_page.html', {'song': song, 'albums': albums, 'saved_songs': saved_songs})

@login_required
def song_form(request):
    """Song form"""
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            song = form.save(commit=False)
            song.posted_by = request.user  # Assign uploader
            song.save()
            return redirect('song_catalog')
    else: 
        form = SongForm()

    return render(request, 'playground/song_form.html', {'form': form})

@login_required
def song_delete(request, song_id):
    """Delete song"""
    song = get_object_or_404(Song, id=song_id)
    song.delete()  # Delete song

    return redirect('song_catalog')
