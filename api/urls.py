from rest_framework.routers import DefaultRouter

from .views import (ArtistAPIView,
                    AlbomAPIView, AlbomDetailAPIView, SongAPIViewSET)

from django.urls import path, include

router = DefaultRouter()
router.register(r'songs', SongAPIViewSET)
router.register(r'artists', ArtistAPIView)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('albom/', AlbomAPIView.as_view(), name='album'),
    path('albom/<int:id>/', AlbomDetailAPIView.as_view(), name='albom-detail'),
]