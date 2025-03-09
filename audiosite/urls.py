from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),

    # User management
    path('user/', include('users.urls')),

    # Home page
    path('', include('main.urls')),

    # Content
    path('content/', include('playground.urls')),

    # Saved songs
    path('saved/', include('saved.urls')),

    # Albums
    path('album/', include('albums.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
