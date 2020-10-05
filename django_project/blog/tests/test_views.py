from django.test import TestCase, Client
from django.urls import reverse
from blog.models import Post
import accessibility_package
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('post_list')


    # def test_view_posts_get(self):
    #     client = Client()
    #     response = self.client.get(self.url)
    #     print(response.content)
        

    def teste_importe_pacote(self):
        client = Client()
        response = self.client.get(self.url)
        print("importou \n\n")
        accessibility_package.teste_import(response.content)