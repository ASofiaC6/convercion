#importamos la la libreta Math
import math

#Se crean las funciones de las operaciones
def dolar(num1):
    return num1*0.052

def libras(num1):
    return num1*0.039

def argentino(num1):
    return num1*50.15

def bolivar(num1):
    return num1*1.91

def euro(num1):
    return num1*0.047

while True:
    print("Convertidor de divisas")
    print("Elija una operación")
    print("a) Pesos a dólares")
    print("b) Pesos a libras esterlinas")
    print("c) Pesos a pesos argentinos")
    print("d) Pesos a bolivares")
    print("e) Pesos a euros")
    print("f) Salir")

    #pedimos la operación al usuario
    opcion=input("Ingrese la opción(a,b,c,d,e,f):")

    #Ejecutamos la operación correspondiente
    if opcion in ["a","b","c","d","e"]:
        num1=float(input("Ingresar el número de pesos: "))

        if opcion=="a":
            resultado=dolar(num1)
            print("el resultado es: ",resultado)

        elif opcion=="b":
            resultado=libras(num1)
            print("el resultado es: ",resultado)

        elif opcion=="c":
            resultado=argentino(num1)
            print("el resultado es: ",resultado)

        elif opcion=="d":
            resultado=bolivar(num1)
            print("el resultado es: ",resultado)

        elif opcion=="e":
            resultado=euro(num1)
            print("el resultado es: ",resultado)

    elif opcion=="f":
        print("Saliendo del programa")
        break
    else:
        print("Opción invalida")

    input("presione Enter para continuar...")
