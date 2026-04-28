import random
import time
import os

HP_INICIAL = 300

nombre1 = input("Nombre Jugador 1: ")
nombre2 = input("Nombre Jugador 2: ")
nombre3 = input("Nombre Jugador 3: ")

j1 = HP_INICIAL
j2 = HP_INICIAL
j3 = HP_INICIAL


def barra(hp):
    bloques = hp // 5
    return "💖" * bloques + "-" * (60 - bloques)


def limpiar():
    os.system("cls" if os.name == "nt" else "clear")


def mostrar():
    print("ESTADO DEL COMBATE\n")
    print(f"{nombre1}: {j1} HP |{barra(j1)}|")
    print(f"{nombre2}: {j2} HP |{barra(j2)}|")
    print(f"{nombre3}: {j3} HP |{barra(j3)}|")


turno = 1

while True:
    if (j1 <= 0 and j2 <= 0) or (j1 <= 0 and j3 <= 0) or (j2 <= 0 and j3 <= 0):
        break

    limpiar()
    print(f"TURNO {turno}\n")

    d1 = random.randint(7, 18)
    d2 = random.randint(7, 18)
    d3 = random.randint(7, 18)

    j2 -= d1
    j3 -= d1

    j1 -= d2
    j3 -= d2

    j1 -= d3
    j2 -= d3

    j1 = max(0, j1)
    j2 = max(0, j2)
    j3 = max(0, j3)

    mostrar()

    print(f"\n{nombre1} hace {d1} daño")
    print(f"{nombre2} hace {d2} daño")
    print(f"{nombre3} hace {d3} daño")

    turno += 1
    time.sleep(1)


print("\nFIN DEL COMBATE\n")

if j1 > 0 and j2 <= 0 and j3 <= 0:
    print(f"Ganador: {nombre1}")
elif j2 > 0 and j1 <= 0 and j3 <= 0:
    print(f"Ganador: {nombre2}")
elif j3 > 0 and j1 <= 0 and j2 <= 0:
    print(f"Ganador: {nombre3}")
else:
    print("No hay ganador claro")