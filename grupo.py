import random
import re

# Leer un archivo de texto y transformarlo en un array
def leer_archivo_como_array(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        lineas = archivo.readlines()
        return [linea.strip() for linea in lineas]

# Definir la dificultad del juego
def seleccionar_dificultad():
    dificultad = input("Selecciona la dificultad: facil, medio, dificil: ").lower()
    while dificultad not in ["facil", "medio", "dificil"]:
        print("Por favor, selecciona una dificultad valida")
        dificultad = input("ingresa la dificultad: facil, medio, dificil: ")
    return dificultad

# Definir los parametros del juego segun la dificultad
def set_parametros(dificultad):
    if dificultad == "facil":
        return {"vidas": 3, "ruta_archivo": './palabras_facil.txt'}
    elif dificultad == "medio":
        return {"vidas": 5, "ruta_archivo": './palabras_medio.txt'}
    elif dificultad == "dificil":
        return {"vidas": 7, "ruta_archivo": './palabras_dificil.txt'}