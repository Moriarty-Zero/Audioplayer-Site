from django.contrib.auth.models import User
from playground.models import Song
from django.db import models
import os
from django.conf import settings

class UserProfile(models.Model):
    # Establishes a one-to-one relationship with the User model.
    # If the user is deleted, the profile is also removed.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def song_save(self, song):
        """
        Saves a song to the user's saved songs list.
        If the song is already saved, it does nothing.
        Otherwise, it creates a new SavedSong entry with default values.
        """
        SavedSong.objects.get_or_create(
            original_song=song,
            user_profile=self,
            defaults={
                'title': song.title,         # Copy the song title
                'cover_image': song.cover_image,  # Copy the cover image
                'audio': song.audio,         # Copy the audio file
                'video': song.video,         # Copy the video file (if available)
            }
        )

    def song_delete(self, song):
        """
        Removes a song from the user's saved songs list.
        Returns True if a song was deleted, False otherwise.
        """
        deleted, _ = SavedSong.objects.filter(original_song=song, user_profile=self).delete()
        return deleted > 0  # Returns True if at least one record was deleted

    def __str__(self):
        """Returns the username as the string 
        representation of the profile. """
        return self.user.username

    
class SavedSong(models.Model):
    """Model for save song"""
    original_song = models.ForeignKey(Song, on_delete=models.CASCADE)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='saved_songs')

    title = models.CharField(max_length=50, default='Untitled Song')
    cover_image = models.ImageField(upload_to='saved_covers/', blank=True, null=True)
    audio = models.FileField(upload_to='saved_audio/')
    video = models.FileField(upload_to='saved_videos/', blank=True, null=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posted_songs')

    def __str__(self):
        return f'{self.user_profile.user.username} = {self.title} - {self.posted_by}'