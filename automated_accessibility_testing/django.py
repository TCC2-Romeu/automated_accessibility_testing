from django.test import TestCase, Client
from django.urls import reverse
from blog.models import Post
import automated_accessibility_testing
import json

__all__ = ["AcessibilityTest"]


class AcessibilityTest(TestCase):
    def setUp(self):
        self.client = Client()

    def assert_acessible_url(self, url: str):
        self.url = reverse(url)
        response = self.client.get(self.url)
        self.assertFalse(
            automated_accessibility_testing.check_accessibility(
                response.content.decode("utf8"), []
            )
        )

    def assert_acessible_fragment(self, fragment: str):
        self.assertFalse(
            automated_accessibility_testing.check_accessibility(fragment, [])
        )

    def assert_static_html_page(self, url: str):
        self.url = reverse(url)
        response = self.client.get(self.url)
        list = ["alt_att_check", "contains_h1", "headers_tag_hierarchy"]
        self.assertFalse(
            automated_accessibility_testing.check_accessibility(
                response.content.decode("utf8"), list
            )
        )
