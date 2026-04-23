def calcular_promedio():
    cantidad = int(input("Cantidad de notas: "))
    suma = 0

    for i in range(cantidad):
        nota = float(input(f"Ingrese la nota {i+1}: "))
        suma += nota

    return suma / cantidad


def evaluar_aprobacion(promedio):
    print("Promedio:", round(promedio, 2))

    if promedio >= 4:
        print("El alumno aprueba")
    else:
        print("El alumno reprueba")


def procesar_estudiantes():
    estudiantes = int(input("Cantidad de estudiantes: "))

    for e in range(estudiantes):
        print(f"\nEstudiante {e+1}")

        promedio = calcular_promedio()
        evaluar_aprobacion(promedio)


procesar_estudiantes()