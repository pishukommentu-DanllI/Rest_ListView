# Generated by Django 4.1.2 on 2023-03-09 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firts_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('patronymic', models.CharField(max_length=255, verbose_name='Отчество')),
                ('birthday', models.DateField(verbose_name='Дата рождения')),
            ],
            options={
                'verbose_name': 'Рижессер',
                'verbose_name_plural': 'Рижессеры',
            },
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название фильм')),
                ('date', models.DateField(verbose_name='Дата выхода')),
                ('country', models.CharField(max_length=255, verbose_name='Страна производителя')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.director', verbose_name='Режиссер')),
            ],
            options={
                'verbose_name': 'Фильм',
                'verbose_name_plural': 'Фильмы',
            },
        ),
        migrations.CreateModel(
            name='Kind',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Жанр')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='Poster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.film', verbose_name='Фильм')),
            ],
            options={
                'verbose_name': 'Фильм',
                'verbose_name_plural': 'Фильмы',
            },
        ),
        migrations.AddField(
            model_name='film',
            name='kind',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.kind', verbose_name='Жанр'),
        ),
    ]