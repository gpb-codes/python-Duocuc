estudiantes = int(input("Cantidad de estudiantes: "))

for e in range(estudiantes):
    print(f"\nEstudiante {e+1}")

    cantidad = int(input("Cantidad de notas: "))
    suma = 0

    for i in range(cantidad):
        nota = float(input(f"ingresa la nota {i+1}: "))
        suma += nota

    promedio = suma / cantidad
    print("Promedio:", round(promedio, 2))

    if promedio >= 4:
        print("Aprueba")
    else:
        print("Reprueba")