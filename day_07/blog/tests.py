from django.test import TestCase, TransactionTestCase
from django.urls import reverse
from django.test.client import Client
from django.contrib.auth.models import User

from blog.models import Article, UserFavouriteArticle


class TestCalls(TransactionTestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('Nik', 'test@test.com', 'test')
        self.art = Article.objects.create(
            title=f'Test',
            author=self.user,
            synopsis=f'synopsis_test',
            content='lorem ipsum test',
        )

    def test_user_anonymous(self):
        response = self.client.get(reverse('favourite'), follow=True)
        self.assertRedirects(response, reverse('login') + f'?next={reverse("favourite")}')
        response = self.client.get(reverse('publication'), follow=True)
        self.assertRedirects(response, reverse('login') + f'?next={reverse("publication")}')
        response = self.client.post(reverse('publish'), follow=True)
        self.assertRedirects(response, reverse('login') + f'?next={reverse("publish")}')

    def test_auth_user_get_post_register(self):
        self.client.login(username='Nik', password='test')
        response = self.client.get(reverse('signup'), follow=True)
        self.assertRedirects(response, reverse('articles'))
        response = self.client.post(reverse('signup'), follow=True)
        self.assertRedirects(response, reverse('articles'))

    def test_auth_user_post_favourite_second(self):
        self.client.login(username='Nik', password='test')
        response = self.client.post(reverse('add_fav', kwargs={'pk': self.art.pk}), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('favourite'))
        self.initial_len = len(UserFavouriteArticle.objects.all())
        response = self.client.post(reverse('add_fav', kwargs={'pk': self.art.pk}), follow=True)
        self.assertEqual(response.status_code, 200)
        finish_len = len(UserFavouriteArticle.objects.all())
        self.assertEqual(self.initial_len, finish_len)
