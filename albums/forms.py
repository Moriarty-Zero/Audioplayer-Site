from .models import Album
from django import forms

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = [
            'title',
            'about',
            'album_image',
            'author'
        ]