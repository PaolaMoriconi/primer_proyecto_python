##Proyecto: Juego de ahorcado
##Integrantes:Noeli Paola Moriconi y Gisele Lorena Ortiz
##Importo random para seleecionar de forma aleatoria una indice del array con las palabras del archivo
import random

##importo re para validar que la letra ingresada sea una letra y no un numero o caracter especial
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
    
# Capturar la letra ingresando por el usuario
def capturar_letra():
    letra = input("Ingresa una letra: ")
    while not re.match("^[a-zA-Z]*$", letra) or len(letra) != 1:
        print("Por favor, ingresa una letra valida")
        letra = input("Ingresa una letra: ")
    return letra

#Seteo parametros
dificultad = seleccionar_dificultad()
parametros = set_parametros(dificultad)
vidas = parametros["vidas"]
ruta_archivo = parametros["ruta_archivo"]

# Leer el archivo y transformarlo en un array
array_lineas = leer_archivo_como_array(ruta_archivo)

#capturo la longitud del array
longitud = len(array_lineas)

# Asignar un número aleatorio
numero_aleatorio = random.randint(0, longitud - 1)
#selecciono una palabra aleatoria del array
palabra_selecionada = array_lineas[numero_aleatorio]

#Inicializo variable que indica si el juego termino
end_game = False
caracteres_incorrectos = []
respuesta = ['_'] * len(palabra_selecionada)

print(f"La palabra seleccionada contiene {len(palabra_selecionada)} caracteres")
print("\n")

