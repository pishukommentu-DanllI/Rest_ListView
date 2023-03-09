from rest_framework.serializers import ModelSerializer
from .models import *


class DirectorSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Director


class KindSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Kind


class FilmSerializer(ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Film

    def to_representation(self, instance):
        representation = super(FilmSerializer, self).to_representation(instance)
        representation['director'] = DirectorSerializer(instance.director, many=False).data
        representation['kind'] = KindSerializer(instance.kind, many=False).data
        return representation


class PosterSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Poster

    def to_representation(self, instance):
        representation = super(PosterSerializer, self).to_representation(instance)
        representation['film'] = FilmSerializer(instance.film, many=False).data
        return representation
