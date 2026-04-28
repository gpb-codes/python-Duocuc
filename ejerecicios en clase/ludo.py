# LUDO 
# 1 jugador juega, y lanza dos dados
# por cada unidad en el dado avanza esa cantidad de casillas
# cuando llegue a 30 casillas gana
# mostrar cuantos turnos le tomo ganar
# Bonus: mostrar el progreso del jugador con un tablero visual
import random
import time
import os

OBJETIVO = 30
posicion = 0
turnos = 0

while posicion < OBJETIVO:
    input("\nPresiona Enter para lanzar los dados...")

    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    avance = dado1 + dado2

    posicion += avance
    turnos += 1

    if posicion > OBJETIVO:
        posicion = OBJETIVO

    os.system("cls" if os.name == "nt" else "clear")

    print(f"Turno: {turnos}")
    print(f"Dados: {dado1} y {dado2}")
    print(f"Avanza: {avance}")
    print(f"Posición: {posicion}/{OBJETIVO}")

    tablero = "-" * OBJETIVO
    tablero = tablero[:posicion-1] + "🦿" + tablero[posicion:]
    print("\n[" + tablero + "]")

    time.sleep(0.5)

print("\nJuego terminado")
print(f"Ganaste en {turnos} turnos")