from django.test import TestCase

from main.models import Cars


class CarsModelsTestCase(TestCase):

    def create_cars(self,id=1,brand='Toyota'):
        return Cars.objects.create(id=id,brand=brand)

    def test_cars_creation(self):
        car = self.create_cars()
        self.assertTrue(isinstance(car,Cars))
        self.assertEqual(car.__str__(),car.brand)

