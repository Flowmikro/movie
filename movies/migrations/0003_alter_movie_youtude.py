# Generated by Django 4.1.7 on 2023-04-17 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie_youtude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='youtude',
            field=models.TextField(),
        ),
    ]
