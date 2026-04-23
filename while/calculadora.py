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
            
            suma = a + b
            print("Resultado:", suma) 
        case "2":
            resta = a - b
            print("Resultado:", resta)
        case "3":
            multiplicacion = a * b
            print("Resultado:", multiplicacion)
        case "4":
            if b != 0:
                dividir = a / b
                print("Resultado:", dividir )
            else:
                print("Error: división por cero no es permitida")
        case _:
            print("Opción inválida")