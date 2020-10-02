from django.test import TestCase, Client
from django.urls import reverse
from blog.models import Post
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('post_list')


    def test_view_posts_get(self):
        client = Client()
        response = self.client.get(self.url)
        print(response.content)
        
