# Generated by Django 4.2 on 2023-05-11 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_remove_movie_youtude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(blank=True, upload_to='movies/', verbose_name='Постер'),
        ),
    ]