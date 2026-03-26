
def suma(a, b, c, d, e):
    return a + b + c + d + e


def promedio(a, b, c, d, e):
    return (a + b + c + d + e) / 5


def volumen(a, b, c, d, e):
    return a * b * c * d * e


def operacion(a, b, c, d, e):
    return (a + b) * (c + d) - e


def polinomio(a, b, c, d, e):

    x = 2  
    return a*x*4 + b*x*3 + c*x*2 + d*x + e


print(suma(1, 2, 3, 4, 5))
print(promedio(5, 10, 15, 20, 25))
print(volumen(1, 2, 3, 4, 5))
print(operacion(2, 3, 4, 5, 6))
print(polinomio(1, 1, 1, 1, 1))
def suma(a, b, c, d, e):
    return a + b + c + d + e

def promedio(a, b, c, d, e):
    return (a + b + c + d + e) / 5

def volumen(a, b, c, d, e):
    return a * b * c * d * e

def operacion(a, b, c, d, e):
    return (a + b) * (c + d) - e

def polinomio(a, b, c, d, e):
    x = 2
    return a*x*4 + b*x3 + c*x*2 + d*x + e


print("=== MENÚ MATEMÁTICO ===")
print("1. Suma")
print("2. Promedio")
print("3. Volumen")
print("4. Operación")
print("5. Polinomio")

opcion = int(input("Elegí una opción (1-5): "))

a = float(input("Ingrese el valor 1: "))
b = float(input("Ingrese el valor 2: "))
c = float(input("Ingrese el valor 3: "))
d = float(input("Ingrese el valor 4: "))
e = float(input("Ingrese el valor 5: "))

if opcion == 1:
    print("Resultado:", suma(a, b, c, d, e))
elif opcion == 2:
    print("Resultado:", promedio(a, b, c, d, e))
elif opcion == 3:
    print("Resultado:", volumen(a, b, c, d, e))
elif opcion == 4:
    print("Resultado:", operacion(a, b, c, d, e))
elif opcion == 5:
    print("Resultado:", polinomio(a, b, c, d, e))
else:
    print("Opción inválida")



    #Oliva Máximo, Zárate Facundo, Fernández Máximo, Acosta Benjamín y Canovas Jeremías