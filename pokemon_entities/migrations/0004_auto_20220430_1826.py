# Generated by Django 3.1.14 on 2022-04-30 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0003_auto_20220430_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='description',
            field=models.TextField(blank=True, max_length=700, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title',
            field=models.TextField(max_length=25, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_en',
            field=models.TextField(blank=True, max_length=25, verbose_name='Английское название'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_jp',
            field=models.TextField(blank=True, max_length=25, verbose_name='Японское название'),
        ),
    ]
