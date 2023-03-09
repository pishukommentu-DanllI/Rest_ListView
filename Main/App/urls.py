from django.urls import path
from .views import *

urlpatterns = [
    path('', ShowRequests.as_view()),
    path('DirectionListCreate/', DirectorListView.as_view()),
    path('DirectionGeneral/<int:pk>/', DirectorRetrieveUpdateDestroyAPIView.as_view()),

    path('KindListCreate/', KindListView.as_view()),
    path('KindGeneral/<int:pk>/', KindRetrieveUpdateDestroyAPIView.as_view()),

    path('FilmListCreate/', FilmListView.as_view()),
    path('FilmGeneral/<int:pk>/', FilmRetrieveUpdateDestroyAPIView.as_view()),

    path('PosterListCreate/', PosterListView.as_view()),
    path('PosterGeneral/<int:pk>/', PosterRetrieveUpdateDestroyAPIView.as_view()),
]
