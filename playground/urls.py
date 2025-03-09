from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    #Song catalog page
    path('song_catalog/', views.song_catalog, name='song_catalog'),

    #Song page
    path('song_page/<int:song_id>/', views.song_page, name='song_page'),

    #Song form page
    path('song_form/', views.song_form, name='song_form'),

    #Delete song
    path('song_delete/<int:song_id>/', views.song_delete, name='song_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)