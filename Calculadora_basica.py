def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: Division por cero"
    else:
        return a / b

def menu():
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    opcion = int(input("Ingrese la opcion deseada: "))
    return opcion

opcion = menu()

if opcion == 1:
    digito1 = int(input("Ingrese un numero para calcular: "))
    digito2 = int(input("Ingrese un numero para calcular: "))
    resultado = suma(digito1, digito2)
    print(f"La suma de {digito1} y {digito2} es: {resultado}")

elif opcion == 2:
    digito1 = int(input("Ingrese un numero para calcular: "))
    digito2 = int(input("Ingrese un numero para calcular: "))
    resultado = resta(digito1, digito2)
    print(f"La resta de {digito1} y {digito2} es: {resultado}")

elif opcion == 3:
    digito1 = int(input("Ingrese un numero para calcular: "))
    digito2 = int(input("Ingrese un numero para calcular: "))
    resultado = multiplicacion(digito1, digito2)
    print(f"La multiplicacion de {digito1} y {digito2} es: {resultado}")

elif opcion == 4:
    digito1 = int(input("Ingrese un numero para calcular: "))
    digito2 = int(input("Ingrese un numero para calcular: "))
    resultado = division(digito1, digito2)
    print(f"La division de {digito1} y {digito2} es: {resultado}")