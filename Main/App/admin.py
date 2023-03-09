from django.contrib import admin
from .models import *


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('id', 'firsts_name', 'last_name', 'patronymic', 'birthday')
    list_editable = ('firsts_name', 'last_name', 'patronymic', 'birthday')


@admin.register(Kind)
class KindAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_editable = ('name',)


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date', 'country', 'director', 'kind')
    list_editable = ('name', 'date', 'country', 'director', 'kind')


@admin.register(Poster)
class PosterAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'film')
    list_editable = ('date', 'film')
