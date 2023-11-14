from django.http import HttpResponse
from django.test import TestCase
from django.urls import reverse


class MainTestCase(TestCase):

    def test_main(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)


class SearchTestCase(TestCase):

    def test_search(self):
        url = reverse('search-car')
        response = self.client.get(url)
        self.assertIsInstance(response,HttpResponse)
        self.assertEqual(200,response.status_code)




