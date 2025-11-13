#Importacion de archivos
from Functions import suma
from calculos import area_cuadrado, area_triangulo, area_circulo

#Programa
print("PRACTICA GIT - 13-11-2025")
#Se realiza un menu para verifica las funciones
menuActivo = True
while menuActivo:
    print("Seleccione una opcion:")
    print("1. Sumar")
    print("2. Area del triangulo")
    print("3. Area del cuadrado")
    print("4. Area del circulo")
    print("5. Salir")
    #Se solicita que ingrese la opcion que va a elegir
    opcion = input("Ingrese el numero de la opcion: ")
    
    if opcion == "1":
        #Solicitud de datos para realizar la suma
        numero1 = float(input("Ingrese el primer numero: "))
        numero2 = float(input("Ingrese el segundo numero: "))
        resultado = suma(numero1, numero2)
        print("Total de la suma:", resultado)
        
    elif opcion == "2":
        #Solicitud de datos para calcular el area del triangulo
        base = float(input("Ingrese la base del triangulo: "))
        altura = float(input("Ingrese la altura del triangulo: "))
        area = area_triangulo(base, altura)
        print("El area del triangulo es:", area)
        
    elif opcion == "3":
        #Solicitud de datos para calcular el area del cuadrado
        lado = float(input("Ingrese el lado del cuadrado: "))
        area = area_cuadrado(lado)
        print("El area del cuadrado es:", area)
    
    elif opcion == "4":
        #Solicitud de datos para calcular el area del circulo
        radio = float(input("Ingrese el lado del circulo: "))
        area = area_circulo(radio)
        print("El area del circulo es:", area)
   
    elif opcion == "5":
        #Con esta opcion se sale del programa
        print("Saliendo del programa...")
    break

