from django.test import TestCase, Client
from django.urls import reverse
from blog.models import Post
import accessibility_package
import json

# Criar uma classe accessibility class case
# onde já faça o bioler plate
# SUbclasse do testcase
# O cliente que importar assertAcessibleURL, assertHTML recebe o html bruto
# url como argumento do metodo
# Popular o readme do pacote
# Distribuir o pacote


class TestViews(TestCase):
    def setUp(self):
        # popular db
        self.client = Client()
        self.url = reverse("post_list")

    def tearDown(self):
        pass
        #  apagar db

    def teste_importe_pacote(self):
        client = Client()
        response = self.client.get(self.url)
        # response.content -- > byte string
        # VErificar se é possivel retornar linha coluna do erro
        list = []
        self.assertFalse(
            accessibility_package.check_accessibility(
                response.content.decode("utf8"), list
            )
        )
