from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.TextField()
    title_en = models.TextField(null=True, blank=True)
    title_jp = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    previous_evolution = models.ForeignKey('Pokemon', on_delete=models.SET_NULL, null=True, blank=True, related_name='prev_pokemon')
    next_evolution = models.ForeignKey('Pokemon', on_delete=models.SET_NULL, null=True, blank=True, related_name='next_pokemon')

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    appeared_at = models.DateTimeField(null=True, blank=True)
    disappeared_at = models.DateTimeField(null=True, blank=True)
    level = models.IntegerField(null=True, blank=True)
    health = models.IntegerField(null=True, blank=True)
    strength = models.IntegerField(null=True, blank=True)
    defence = models.IntegerField(null=True, blank=True)
    stamina = models.IntegerField(null=True, blank=True)


