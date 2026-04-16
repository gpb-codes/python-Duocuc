print("Tienda-If")
total=0
print("Productos disponibles:")
print("1. Cereal 2000")
print("2. Lechuga 1800")
print("3. Leche 1000")

producto=int(input("elige un producto (escribe un numero): "))

if producto == 1:
    print("has eligido el cereal: ")
    total += 2000*1.19
elif producto == 2:
    print("has eligido la lechuga: ")
    total += 1800*1-19
elif producto == 3:
    print("has eligido la leche: ")
    total += 1000*1.19
else:
    print("producto no existente")

print("total a pagar", total)
