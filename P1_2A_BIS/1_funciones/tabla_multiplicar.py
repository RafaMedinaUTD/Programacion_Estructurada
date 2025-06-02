#TAREA: 
#Crear una tabla de multiplicar del 2 que no use funciones ni estructuras de control

print("2 x 1 =", 2 * 1)

print("2 x 2 =", 2 * 2)

print("2 x 3 =", 2 * 3)

print("2 x 4 =", 2 * 4)

print("2 x 5 =", 2 * 5)

print("2 x 6 =", 2 * 6)

print("2 x 7 =", 2 * 7)

print("2 x 8 =", 2 * 8)

print("2 x 9 =", 2 * 9)

print("2 x 10 =", 2 * 10)

print("Presiona enter para continuar")
input()
#crea una tabla de multiplicar del 2 que use funciones y estructuras de control
import os
os.system("clear")


def tabla_multiplicar_2(numero):
    num=numero
    respuesta=""
    for i in range(1, 11):
        respuesta+=f"{num} x {i} = {num * i}\n"
    return respuesta

numero=int(input("Introduzca el numero de la tabla de multiplicar que deseas calcular: "))
print(f"tabla del {numero}")
resultado=tabla_multiplicar_2(numero)
print(f"{resultado}")
