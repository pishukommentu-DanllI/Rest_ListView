from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import *


class ShowRequests(APIView):
    requests = {
        'Create Direction or show all Directions': 'DirectionListCreate/',
        'Put or Retrieve and delete direction for pk for Direction': 'DirectionGeneral/<int:pk>',

        'Create Kind or show all Kinds': 'KindListCreate/',
        'Put or Retrieve and delete direction pk for Kind': 'KindGeneral/<int:pk>',

        'Create Film or show all Films': 'FilmListCreate/',
        'Put or Retrieve and delete direction for pk for Film': 'FilmGeneral/<int:pk>',

        'Create Poster or show all Posters': 'PosterListCreate/',
        'Put or Retrieve and delete direction for pk for Poster': 'PosterGeneral/<int:pk>'

    }

    def get(self, *args, **kwargs):
        return Response(self.requests)


class DirectionApi:
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class DirectorListView(DirectionApi, ListCreateAPIView):
    """Класс API для Режиссеров ListCreate"""


class DirectorRetrieveUpdateDestroyAPIView(DirectionApi, RetrieveUpdateDestroyAPIView):
    """Класс API для Режиссеров RetrieveUpdate"""


class KinApi:
    queryset = Kind.objects.all()
    serializer_class = KindSerializer


class KindListView(KinApi, ListCreateAPIView):
    """Класс API для Жанра ListCreate"""


class KindRetrieveUpdateDestroyAPIView(KinApi, RetrieveUpdateDestroyAPIView):
    """Класс API для Жанра RetrieveUpdateDestroyAPIView"""


class FilmApi:
    queryset = Film.objects.all()
    serializer_class = FilmSerializer


class FilmListView(FilmApi, ListCreateAPIView):
    """Класс API для Фильма ListCreate"""


class FilmRetrieveUpdateDestroyAPIView(FilmApi, RetrieveUpdateDestroyAPIView):
    """Класс API для Фильма RetrieveUpdateDestroyAPIView"""


class PosterApi:
    queryset = Poster.objects.all()
    serializer_class = PosterSerializer


class PosterListView(PosterApi, ListCreateAPIView):
    """Класс API для Афиши ListCreate"""


class PosterRetrieveUpdateDestroyAPIView(PosterApi, RetrieveUpdateDestroyAPIView):
    """Класс API для Афиши RetrieveUpdateDestroyAPIView"""
