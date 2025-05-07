import os
import random
from flask import Flask

app = Flask(__name__)


def cuadricula():
    filas = 5
    columnas = 5
    tablero = [[random.randint(0, 1) for _ in range(columnas)] for _ in range(filas)]
    return tablero


def contarvecinos(tablero, fila, columna):
    filas = len(tablero)
    columnas = len(tablero[0])
    vecinos_vivos = 0

    for i in range(fila - 1, fila + 2):
        for j in range(columna - 1, columna + 2):
            if i == fila and j == columna:
                continue

            if 0 <= i < filas and 0 <= j < columnas:
                vecinos_vivos += tablero[i][j]

    return vecinos_vivos


tablero = cuadricula()

@app.route("/")
def siguiente_generacion():
    filas = len(tablero)
    columnas = len(tablero[0])
    nuevo_tablero = [[0 for _ in range(columnas)] for _ in range(filas)]

    for i in range(filas):
        for j in range(columnas):
            vecinos = contarvecinos(tablero, i, j)
            celda = tablero[i][j]

            # Reglas del Juego de la Vida
            if celda == 1:
                if vecinos == 2 or vecinos == 3:
                    nuevo_tablero[i][j] = 1  # sobrevive
                else:
                    nuevo_tablero[i][j] = 0  # muere
            else:
                if vecinos == 3:
                    nuevo_tablero[i][j] = 1  # nace
                else:
                    nuevo_tablero[i][j] = 0  # sigue muerta

    return nuevo_tablero
