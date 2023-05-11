from django.test import TestCase
from .models import *
from django.urls import reverse


class MovieViewTest(TestCase):
    def test_get(self):
        resp = self.client.get(reverse('movie_list'))
        self.assertEquals(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'movies/movie_list.html')


class MovieDetailViewTest(TestCase):
    def test_get(self):
        movie = Movie.objects.create(title='Test Movie', url='test-movie')
        resp = self.client.get(reverse('movie_detail', kwargs={'slug': movie.url}))
        # resp = self.client.get(reverse('movie_detail'))
        self.assertEquals(resp.status_code, 200)
        self.assertEquals(resp, 'movies/movie_detail.html')

# class MovieViewTest(TestCase):
#
#     def setUp(self) -> None:
#         Category.objects.create(name='это другой тест')
#
#     def test_view_url_exists_proper_location(self):
#         resp = self.client.get('/')
#         self.assertEquals(resp.status_code, 200)
#
#
#     def test_views_uses_correct_template(self):
#         resp = self.client.get(reverse('movie_list'))
#         self.assertEquals(resp.status_code, 200)
#         self.assertTemplateUsed(resp, 'movies/movie_list.html')
