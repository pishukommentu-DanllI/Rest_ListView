from django.db import models


class Director(models.Model):
    firsts_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=255, verbose_name='Отчество')

    birthday = models.DateField(verbose_name='Дата рождения')

    def __str__(self):
        return f'{self.last_name} {self.firsts_name} {self.patronymic}'

    class Meta:
        verbose_name = 'Режиссер'
        verbose_name_plural = 'Режиссеры'


class Kind(models.Model):
    name = models.CharField(max_length=255, verbose_name='Жанр')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Film(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название фильм')

    date = models.DateField(verbose_name='Дата выхода')

    country = models.CharField(max_length=255, verbose_name='Страна производителя')

    director = models.ForeignKey(Director, verbose_name='Режиссер', on_delete=models.CASCADE)

    kind = models.ForeignKey(Kind, verbose_name='Жанр', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


class Poster(models.Model):
    date = models.DateField(verbose_name='Дата')

    film = models.ForeignKey(Film, verbose_name='Фильм', on_delete=models.CASCADE)

    def __str__(self):
        return f'{str(self.film)} {self.date}'

    class Meta:
        verbose_name = 'Афиша'
        verbose_name_plural = 'Афиша'
