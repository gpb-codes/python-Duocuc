pin = int(input("Crea un pin de 4 dígitos: "))

if len(str(pin)) == 4:
    print("Pin válido")
else:
    print("El pin debe tener exactamente 4 dígitos")
    print("Tu pin no es válido")