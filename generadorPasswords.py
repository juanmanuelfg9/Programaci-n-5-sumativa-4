#Programar en Python un generador de contraseñas aleatorio.Por Juan Fernandez. Para  programacion V-UBA
#Se importa la libreria random
import random
#Se declaran variables
minuscula ='abcdefghijklmnopqrstuvwxyz'
mayuscula = minuscula.upper()
simbolos = '!#$%&()*+,-./:;<=>?@[]^_{|}~'
basedelgenerador =minuscula+mayuscula+simbolos
longitud = 14

print("Bienvenido a tu generador de contraseñas favorito")
#Se solicita la cantidad de contraseñas aleatorias a generar
numero = int(input("Cuantas contraseñas necesitas generar? "))


#Se generan las contraseñas
for _ in range(numero):
    #En esta variable se guardan 14 digitos aleatorios
    prototipo = random.sample(basedelgenerador,longitud)
    #En esta variable se concatenan los 14 digitos aleatorios
    password = "".join(prototipo)
    #Se imprime la contraseña
    print(password)

