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
    print("\033[1;3m🌟¡Bienvenido al juego del Ahorcado!\033[0m🌟")
    dificultad = input("\033[1;3m Selecciona la dificultad:\033[0m 🟢 Facil, 🟡 Medio,🔴 Dificil: ").lower()
    while dificultad not in ["facil", "medio", "dificil"]:
        print("❌ Por favor, selecciona una dificultad valida")
        dificultad = input("ingresa la dificultad: Facil 🟢, Medio 🟡, Dificil🔴: ")
    return dificultad

# Definir los parametros del juego segun la dificultad
def set_parametros(dificultad):
    if dificultad == "facil":
        return {"vidas": 3 , "ruta_archivo": './palabras_facil.txt'}
    elif dificultad == "medio":
        return {"vidas": 5, "ruta_archivo": './palabras_medio.txt'}
    elif dificultad == "dificil":
        return {"vidas": 7, "ruta_archivo": './palabras_dificil.txt'}
    
# Capturar la letra ingresando por el usuario
def capturar_letra():
    letra = input("🔤Ingresa una letra: ")
    while not re.match("^[a-zA-Z]*$", letra) or len(letra) != 1:
        print("⚠️Por favor, ingresa una letra valida")
        letra = input("🔤Ingresa una letra: ")
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

print(f" La palabra seleccionada contiene {len(palabra_selecionada)} caracteres")
print("\n")

while end_game == False:
    print(f"candidad de vidas {vidas}")
    print("\n")

    if len(caracteres_incorrectos) > 0:
        print(f"los caracteres incorrectos seleccionados son: {caracteres_incorrectos}")
        continuar = input("Desea continuar, ingrese no para abandonar el juego. Con cualquier otra letra continuara: ")
        if continuar.lower() == "no":
            print(f"Decidio abandonar el juego, la palabra era: {palabra_selecionada}. Usted perdio")
            break

    print(''.join(respuesta).upper())
    print("\n")
    
    letra_usuario = capturar_letra().lower()

    if letra_usuario in palabra_selecionada:
        for indice, letra in enumerate(palabra_selecionada):
            if letra == letra_usuario:            
                respuesta[indice] = letra_usuario
        
        print(''.join(respuesta).upper())
        print("\n")
        if respuesta == list(palabra_selecionada):
            end_game = True
            print("Ganaste  🎉")
            print("\n")
    else:
        caracteres_incorrectos.append(letra_usuario)
        print("\033[1;3m La letra no está en la palabra \033[0m")
        print("\n")
        vidas -= 1
    
    if vidas == 0:
        end_game = True
        print(f" 💀Fin del juego, te quedaste sin vidas. La palabra era: {palabra_selecionada}")
        print("\n")
