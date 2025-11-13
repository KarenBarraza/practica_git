#funcion para hallar el area de un triangulo
#le falto completar la formula, se realiza correccion y se añade /2
def area_triangulo(base, altura):
    return base * altura/2
#funcion para hallar el area de un cuadrado
#En la funciones destino dos variables pero solo se usa una, se elimina la variable innecesaria
def area_cuadrado(lado):
    return lado * lado

def area_circulo(radio):
    return 3.1416*(radio**2)