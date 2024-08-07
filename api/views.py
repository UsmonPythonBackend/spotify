from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView, CreateAPIView
from .models import Artist, Albom, Song
from .serializers import ArtistSerializer, AlbomSerializer, SongSerializer


class ArtistAPIView(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [IsAdminUser, ]


class AlbomAPIView(APIView):
    def get(self, request):
        alboms = Albom.objects.all()
        albom_serializer = AlbomSerializer(alboms, many=True)
        return Response(data=albom_serializer.data)

class AlbomDetailAPIView(APIView):
    def get(self, request, id):
        albom = Albom.objects.get(id=id)
        serializer = AlbomSerializer(albom)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, id):

        albom = Albom.objects.get(id=id)
        serializer = AlbomSerializer(instance=albom, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SongAPIViewSET(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    # permission_classes = [IsAuthenticated, ]
