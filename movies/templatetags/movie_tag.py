from django import template
from django.template import library

from movies.models import Category, Movie


register = template.Library()


@register.simple_tag()
def get_category():
    '''Вывод всех категорий'''
    return Category.objects.all()


@register.inclusion_tag('movies/tag/new_movies.html')
def get_new_movies():
    movies = Movie.objects.order_by('id')[:5]
    return {'new_movies': movies}

