from django.test import TestCase
from .models import City

class CityModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        City.objects.create(city_name='A City', country='A Country')

    def test_city_name_content(self):
        city = City.objects.get(id=1)
        expected_object_name = f'{city.city_name}'
        self.assertEquals(expected_object_name, 'A City')

    def test_country_content(self):
        city = City.objects.get(id=1)
        expected_object_name = f'{city.country}'
        self.assertEquals(expected_object_name, 'A Country')