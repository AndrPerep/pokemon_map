from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.TextField(verbose_name='Название')
    title_en = models.TextField(null=True, blank=True, verbose_name='Английское название')
    title_jp = models.TextField(null=True, blank=True, verbose_name='Японское название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    image = models.ImageField(null=True, blank=True, verbose_name='Картинка')
    previous_evolution = models.ForeignKey(
        'Pokemon',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='prev_pokemon',
        verbose_name='Предыдущая эволюция')
    next_evolution = models.ForeignKey(
        'Pokemon',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='next_pokemon',
        verbose_name='Следующая эволюция')

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, verbose_name='Покемон')
    lat = models.FloatField(null=True, blank=True, verbose_name='Широта')
    lon = models.FloatField(null=True, blank=True, verbose_name='Долгота')
    appeared_at = models.DateTimeField(null=True, blank=True, verbose_name='Время появления')
    disappeared_at = models.DateTimeField(null=True, blank=True, verbose_name='Время исчезновения')
    level = models.IntegerField(null=True, blank=True, verbose_name='Уровень')
    health = models.IntegerField(null=True, blank=True, verbose_name='Здоровье')
    strength = models.IntegerField(null=True, blank=True, verbose_name='Сила')
    defence = models.IntegerField(null=True, blank=True, verbose_name='Защита')
    stamina = models.IntegerField(null=True, blank=True, verbose_name='Выносливость')


