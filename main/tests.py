from django.test import TestCase, Client
from main.models import Product

class mainTest(TestCase):
    # from tutorial 1
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    # from tutorial 1
    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

    # new testing
    def setUp(self):
        Product.objects.create(name="Holo Charizard", amount="100"
                               , description="Authentic Charizard carfrom 1999", price="4200")
        Product.objects.create(name="Pikachu", amount="500"
                               , description="Mascot of Pokemon", price="10")
