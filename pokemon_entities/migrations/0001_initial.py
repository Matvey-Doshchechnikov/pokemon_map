# Generated by Django 4.2.9 on 2024-03-26 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название (рус.)')),
                ('title_en', models.CharField(blank=True, max_length=200, verbose_name='Название (англ.)')),
                ('title_jp', models.CharField(blank=True, max_length=200, verbose_name='Название (яп.)')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Картинка')),
                ('previous_evolution', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next_evolutions', to='pokemon_entities.pokemon', verbose_name='Предыдущая эволюция')),
            ],
            options={
                'verbose_name': 'Тип покемона',
                'verbose_name_plural': 'Типы покемонов',
            },
        ),
        migrations.CreateModel(
            name='PokemonEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField(verbose_name='Широта')),
                ('lon', models.FloatField(verbose_name='Долгота')),
                ('appeared_at', models.DateTimeField(verbose_name='Время появления')),
                ('disappeared_at', models.DateTimeField(verbose_name='Время исчезновения')),
                ('level', models.IntegerField(blank=True, null=True, verbose_name='Уровень')),
                ('health', models.IntegerField(blank=True, null=True, verbose_name='Здоровье')),
                ('strength', models.IntegerField(blank=True, null=True, verbose_name='Атака')),
                ('defence', models.IntegerField(blank=True, null=True, verbose_name='Защита')),
                ('stamina', models.IntegerField(blank=True, null=True, verbose_name='Выносливость')),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entities', to='pokemon_entities.pokemon', verbose_name='Тип покемона')),
            ],
            options={
                'verbose_name': 'Покемон',
                'verbose_name_plural': 'Покемоны',
            },
        ),
    ]
