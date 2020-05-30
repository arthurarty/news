from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from articles.models import Article


class ArticleTest(APITestCase):

    def test_get_article(self):
        article = Article()
        article.headline = "Getting started"
        article.summary = "Getting Started"
        article.image_url = "https://pixabay.com/images/id-1031754/"
        article.author = "John Doe"
        article.slug = "getting_started"
        article.save()
        url = reverse('articles:index')
        response = self.client.get(url)
        articles = response.json()
        self.assertEqual(200, response.status_code)
        self.assertEqual(articles[0]['headline'], article.headline)
