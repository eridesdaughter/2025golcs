import os
import random
import time
from server import siguiente_generacion, tablero
import requests

r = requests.get('http://192.168.1.10:5000')


datos = r.json()

print(datos)
