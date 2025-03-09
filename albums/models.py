from django.contrib.auth.models import User
from django.db import models
import os
from django.conf import settings

class Album(models.Model):
    '''Album model'''
    title = models.CharField(max_length=50)
    about = models.CharField(max_length=160)
    album_image = models.ImageField(upload_to='covers/')
    author = models.CharField(max_length=70, default='Unknown')
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='albums')

    def __str__(self):
        '''String representation of the album'''
        return f'{self.title} - {self.author}'

    def delete(self, *args, **kwargs):
        '''Override delete to remove related files'''
        file_field = getattr(self, 'album_image', None)
        if file_field and file_field.name:
            file_path = os.path.join(settings.MEDIA_ROOT, file_field.name)
            if os.path.exists(file_path):
                os.remove(file_path)

        super().delete(*args, **kwargs)

