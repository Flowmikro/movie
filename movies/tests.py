from django.test import TestCase
from .models import *
from django.urls import reverse


class ModelCategoryTestCase(TestCase):
    def setUp(self) -> None:
        Category.objects.create(name='Test')

    def test_model_name(self):
        result = Category.objects.get(id=1)
        expected_object_name = f'{result.name}'
        self.assertEquals(expected_object_name, 'Test')


class ModelActorTestCase(TestCase):
    def setUp(self) -> None:
        Actor.objects.create(name='Leo')

    def test_model_name(self):
        result = Actor.objects.get(id=1)
        expected_object_name = f'{result.name}'
        self.assertEquals(expected_object_name, 'Leo')


class ModelGenreTestCase(TestCase):
    def setUp(self) -> None:
        Genre.objects.create(name='Action')

    def test_model_name(self):
        result = Genre.objects.get(id=1)
        expected_object_name = f'{result.name}'
        self.assertEquals(expected_object_name, 'Action')


class ModelMovieTestCase(TestCase):
    def setUp(self) -> None:
        Movie.objects.create(title='Django', poster='img.jp')

    def test_model_name(self):
        result = Movie.objects.get(id=1)
        expected_object_name = f'{result.title}'
        self.assertEquals(expected_object_name, 'Django')


class ModelRatingStarTestCase(TestCase):
    def setUp(self) -> None:
        RatingStar.objects.create(value=4)

    def test_model_name(self):
        result = RatingStar.objects.get(id=1)
        expected_object_name = f'{result.value}'
        self.assertEquals(expected_object_name, '4')


class ModelReviewsTestCase(TestCase):
    def setUp(self) -> None:
        Reviews.objects.create(name='Islam')

    def test_model_name(self):
        result = Reviews.objects.get(id=1)
        expected_object_name = f'{result.name}'
        self.assertEquals(expected_object_name, 'Islam')


class MovieViewTestCase(TestCase):
    def test_get(self):
        resp = self.client.get(reverse('movie_list'))
        self.assertEquals(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'movies/movie_list.html')


class MovieDetailViewTestCase(TestCase):
    def test_get(self):
        movie = Movie.objects.create(title='Test Movie', url='test-movie', poster='sdf.jpg/')
        resp = self.client.get(reverse('movie_detail', kwargs={'slug': movie.url}))
        self.assertEquals(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'movies/movie_detail.html')



