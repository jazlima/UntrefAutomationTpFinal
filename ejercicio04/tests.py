import requests
import unittest

class Test_Pokeapi(unittest.TestCase):

    def setUp(self) -> None:
        self.url = 'https://pokeapi.co/api/v2/'

    def test_get_berry_1(self):
        r = requests.get(self.url+'berry/1/')
        response = r.json()
        self.assertEqual(response['size'], 20)
        self.assertEqual(response['soil_dryness'], 15)
        self.assertEqual(response['firmness'][ 'name'], 'soft')

    def test_get_berry_2(self):
        r = requests.get(self.url+'berry/2/')
        response = r.json()
        self.assertEqual(response['firmness'][ 'name'], 'super-hard')
        self.assertGreater(response['size'], 20)
        self.assertEqual(response['soil_dryness'], 15)
    
    def test_get_pikachu(self):
        r = requests.get(self.url+'pokemon/pikachu/')
        response = r.json()
        self.assertGreater(response['base_experience'], 10)
        self.assertLess(response['base_experience'], 1000)
        self.assertEqual(response['types'][0]['type']['name'], 'electric')







