from django.contrib.auth.models import User
from albums.models import Album
from django.db import models
import os
from django.conf import settings

class Tags(models.TextChoices):
    """Enum class for song tags"""
    NONE = 'none', 'None'
    POP = 'pop', 'Pop'
    MODERN = 'modern', 'Modern'
    ROCK = 'rock', 'Rock'
    HIP_HOP = 'hip-hop', 'Hip-Hop'
    RAP = 'rap', 'Rap'
    JAZZ = 'jazz', 'Jazz'
    ELECTRONIC = 'electronic', 'Electronic'
    ANIME = 'anime', 'Anime'
    CLASSIC = 'classic', 'Classic'
    VIDEO = 'video', 'Video'

class Song(models.Model):
    # Song belongs to an album (optional)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs', null=True, blank=True)
    
    # Basic song details
    title = models.CharField(max_length=50)
    audio = models.FileField(upload_to='songs/')  # Audio file
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True)  # Cover image (optional)
    video = models.FileField(upload_to='videos/', blank=True, null=True)  # Video file (optional)
    
    # Song metadata
    tags = models.CharField(max_length=100, choices=Tags.choices, default=Tags.NONE)  # Genre/tag
    author = models.CharField(max_length=15, default='Unknown')  # Song author
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uploaded_songs')  # Uploader

    def __str__(self):
        return f'{self.title} - {self.author}'

    def delete(self, *args, **kwargs):
        """
        Custom delete method to remove associated files from the server when a song is deleted.
        """
        for field in ['audio', 'cover_image', 'video']:
            file_field = getattr(self, field)
            if file_field and file_field.name:  
                file_path = os.path.join(settings.MEDIA_ROOT, file_field.name)
                if os.path.exists(file_path):
                    os.remove(file_path)  # Delete file from storage

        super().delete(*args, **kwargs)  # Delete the object from the database
