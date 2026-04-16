cantidad = int(input("¿Cuantas notas desa ingresar?: "))

suma = 0

for i in range(cantidad):

    nota = float(input(f"ingrese la nota {i+1}:"))

    suma += nota

    promedio = suma / cantidad
    
print("Promedio:", round(promedio, 2))
if promedio >= 4:
    print("Aprueba")
else:
    print("Reprueba")
    
