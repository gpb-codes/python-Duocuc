def suma():
    print("Resultado:", a + b)
def resta():
    print("Resultado:", a - b)
def multiplicacion():
    print("Resultado:", a * b)
def dividir():
    print("Resultado:", a / b)

while True:
    print("CALCULADORA")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    op = input("Elige una opción: ")

    if op == "5":
        print("Saliendo del sistema...")
        break

    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))

    match op:
        case "1":
            suma()
        case "2":
            resta()
        case "3":
            multiplicacion()
        case "4":
            if b != 0:
                dividir()
            else:
                print("Error: división por cero no es permitida")
        case _:
            print("Opción inválida")