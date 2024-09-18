#importamos la la librerie Math
import math

#Se crean las funciones de las operaciones
def suma(num1,num2):
    return num1+num2

def resta(num1,num2):
    return num1-num2

def multiplicación(num1,num2):
    return num1*num2

def division(num1,num2):
    if num2==0:
        return "Error: División por cero no permitir"
    return num1/num2

while True:
    print("Calculadora Básica")
    print("Elija una operación")
    print("a) Sumar")
    print("b) Restar")
    print("c) Multiplicar")
    print("d) Dividir")
    print("e) Salir")
    
    #pedimos la operación al usuario
    opcion=input("Ingrese la opción(a,b,c,d,e):")

    #Ejecutamos la operación correspondiente
    if opcion in ["a","b","c","d"]:
        num1=float(input("Ingresar el primer número: "))
        num2=float(input("Ingresar el segundo número: "))

        if opcion=="a":
            resultado=suma(num1,num2)
            print("el resultado de la suma es: ",resultado)

        elif opcion=="b":
            resultado=resta(num1,num2)
            print("el resultado de la resta es: ",resultado)

        elif opcion=="c":
            resultado=multiplicación(num1,num2)
            print("el resultado de la multiplicación es: ",resultado)

        elif opcion=="d":
            resultado=division(num1,num2)
            print("el resultado de la división es: ",resultado)

    elif opcion=="e":
        print("Saliendo del programa")
        break
    else:
        print("Opción invalida")

    input("presione Enter para continuar...")

