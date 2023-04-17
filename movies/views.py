from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from django.views.generic.base import View

from .models import *
from .forms import ReviewForm, RatingForm


class MovieView(View):
    '''Список фильмов'''
    template_name = 'movies/movies.html'

    def get(self, request):
        movies = Movie.objects.all()
        return render(request, 'movies/movie_list.html', {'movie_list': movies})


class MovieDetailView(View):
    """Полное описание фильма"""
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['star_form'] = ReviewForm()
        return context

    def get(self, request, slug):
        movie = Movie.objects.get(url=slug)
        return render(request, 'movies/movie_detail.html', {'movie': movie})


class AddReview(View):
    '''Отзывы'''
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = movie
            review.save()
        return redirect('/')


class ActorView(DetailView):
    '''Вывод информации об актере '''
    model = Actor
    template_name = 'movies/actor.html'
    slug_field = 'name'

