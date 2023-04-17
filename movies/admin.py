from django.contrib import admin
from .models import *

from django import forms
from django.contrib import admin


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')
    list_display_links = ('name',)


@admin.register(Actor)
class ACtorAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')
    list_filter = ('category', 'year')
    search_fields = ('title', 'category__name')


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'movie', 'id')
    readonly_fields = ('name', 'email', 'movie')


@admin.register(Genre)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(MovieShots)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'movies',)


@admin.register(Rating)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('star',)


@admin.register(RatingStar)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('value',)



