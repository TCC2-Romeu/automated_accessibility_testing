from django.test import TestCase, Client
from django.urls import reverse
from blog.models import Post
import accessibility_package
import json

class TestViews(TestCase):

    def setUp(self):
        # popular db
        self.client = Client()
        self.url = reverse('post_list')

    def tearDown(self):
        pass
        #  apagar db


    def teste_importe_pacote(self):
        client = Client()
        response = self.client.get(self.url)
        #response.content -- > byte string
        # VErificar se é possivel retornar linha coluna do erro
        list =  ['fc_alt']
        self.assertTrue(accessibility_package.check_accessibility(response.content.decode('utf8'), None))  
