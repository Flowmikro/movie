from django.test import TestCase
from .models import Category
from django.urls import reverse


class MovieModelTest(TestCase):
    def setUp(self):
        Category.objects.create(name='это тест')

    def test_model_name(self):
        post = Category.objects.get(id=1)
        expected_object_name = f'{post.name}'
        self.assertEquals(expected_object_name, 'это тест')


class HomePageViewTest(TestCase):

    def setUp(self) -> None:
        Category.objects.create(name='это другой тест')

    def test_view_url_exists_proper_location(self):
        resp = self.client.get('/')
        self.assertEquals(resp.status_code, 200)

    # def test_view_url_by_name(self):
    #     resp = self.client.get(reverse('movie_list'))
    #     self.assertEquals(resp.status_code, 200)

    def test_views_uses_correct_template(self):
        resp = self.client.get(reverse('movie_list'))
        self.assertEquals(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'movies/movie_list.html')
