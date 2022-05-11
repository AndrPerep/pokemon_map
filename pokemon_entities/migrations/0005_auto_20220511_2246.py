# Generated by Django 3.1.14 on 2022-05-11 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0004_auto_20220430_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='next_evolution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next_pokemons', to='pokemon_entities.pokemon', verbose_name='Следующая эволюция'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='previous_evolution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='prev_pokemons', to='pokemon_entities.pokemon', verbose_name='Предыдущая эволюция'),
        ),
    ]
