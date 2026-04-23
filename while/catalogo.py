op=0
total=0

while op!=4:
    print("1.PC $500.00")
    print("2. LGTV 55 pulgadas $ 380.000")
    print("3. Microondas Hamsa $100.000")
    print("4. Salir")

    op=int(input())
    match op:
        case 1:
            print (" El total a Pagar es ", 500000 *1.19)
            total=5000000 *1.19
        case 2:
            print (" El total a Pagar es ", 3800000 *1.19)
            total=5000000 *1.19
        case 3:
            print (" El total a Pagar es ", 100000 *1.19)
            total=5000000 *1.19
        case 4:
            print (" has seleccionado salir, hasta luego")
        case _:
            print (" opcion no valida, intente de nuevo")