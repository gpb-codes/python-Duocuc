pin = int(input("Crea un pin de 4 dígitos: "))

if 1000 <= pin <= 9999:
    print("Pin válido")
else:
    print("El pin debe tener exactamente 4 dígitos")
    print("Tu pin no es válido")