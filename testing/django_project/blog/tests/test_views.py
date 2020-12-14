from django.test import TestCase, Client
from django.urls import reverse
from blog.models import Post
import automated_accessibility_testing
import json


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("post_list")

    def tearDown(self):
        pass

    def teste_importe_pacote(self):
        client = Client()
        response = self.client.get(self.url)
        list = []
        self.assertFalse(
            automated_accessibility_testing.check_accessibility(
                response.content.decode("utf8"), list
            )
        )
