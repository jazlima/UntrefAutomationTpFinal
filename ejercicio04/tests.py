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
    
    def test_get_pikachu(self):
        r = requests.get(self.url+'pokemon/pikachu/')
        response = r.json()
        self.assertEqual(response['types'][0]['type']['name'], 'electric')

#Caso 1

#Hacer un get a berry/1
#Verificar que el size sea 20
#Verificar que el soil_dryness sea 15
#Verificar que en firmness, el name sea soft.



#r = requests.get('https://pokeapi.co/api/v2/berry/1')
#print(r.json())

#response = r.json()
#print(response['size'])
#cdprint(r.json()['size'])
#Caso 2

#Hacer un get a berry/2
#Verificar que en firmness, el name sea super-hard
#Verificar que el size sea mayor al del punto anterior
#Verificar que el soil_dryness sea igual al del punto anterior



#Caso 3

#Hacer un get a pikachu (https://pokeapi.co/api/v2/pokemon/pikachu/)
#Verificar que su experiencia base es mayor a 10 y menor a 1000
#Verificar que su tipo es “electric”








