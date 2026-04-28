# 3 jugadores juegan golfito,
# cada persona tiene la posibilidad de golpear
# mostrar al final, el golpe mas fuerte
import random

j1 = random.randint(60, 190)
j2 = random.randint(60, 190)
j3 = random.randint(60, 190)

print("Jugador 1:", j1)
print("Jugador 2:", j2)
print("Jugador 3:", j3)

escala = 10

print("\nprogreso de golpes:\n")

print("Jugador 1:", "🏌️" * (j1 // escala))
print("Jugador 2:", "🏌️" * (j2 // escala))
print("Jugador 3:", "🏌️" * (j3 // escala))

max_golpe = max(j1, j2, j3)

print("\nresultado final:")

if max_golpe == j1:
    print("Golpe más fuerte: Jugador 1")
elif max_golpe == j2:
    print("Golpe más fuerte: Jugador 2")
else:
    print("Golpe más fuerte: Jugador 3")