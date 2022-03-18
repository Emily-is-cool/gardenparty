from django.test import TestCase
from .models import Garden, GardenType, Plant
# Create your tests here.

class GardenTest(TestCase):
    def setUp(self):
        self.Garden=Garden(gardenname='spring2022')

    def test_gardenstring(self):
        self.assertEqual(str(self.Garden), 'spring2022')

    def test_tablename(self):
        self.assertEqual(str(Garden._meta.db_table), 'garden')

class GardenTypeTest(TestCase):
    def setUp(self):
        self.GardenType=GardenType(typename='rooftop')

    def test_gardentype(self):
        self.assertEqual(str(self.GardenType), 'rooftop')

    def test_tablename(self):
        self.assertEqual(str(GardenType._meta.db_table), 'gardentype')

class PlantTest(TestCase):
    def setUp(self):
        self.Plant=Plant(plantname='strawberry')

    def test_plant(self):
        self.assertEqual(str(self.Plant.plantname), 'strawberry')

    def test_tablename(self):
        self.assertEqual(str(Plant._meta.db_table), 'plant')
        
        ##Saving this for later...
        ##self.Plant=Plant(plantname='strawberry', plantdescr='everbearing', user=self.user, isseed=True, dateplanted=2022-3-16, dateharvested='null', gardenid=self.gardenid)
