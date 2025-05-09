import os
import requests


def mostrar_tablero(tablero):
    os.system('cls' if os.name == 'nt' else 'clear')  # limpia pantalla
    for fila in tablero:
        print("".join("█" if celda else " " for celda in fila))


r = requests.get('http://192.168.1.10:5000/nuevo-tablero/10/15')





r = requests.get('http://192.168.1.10:5000')
datos = r.json()
mostrar_tablero(datos)
