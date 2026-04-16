
name = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
letrasN = 0

for i in name:
    letrasN += 1

vocales = "aeiouAEIOU"
vocalesN = 0
consonantesN = 0

consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

for letra in name:
    if letra in vocales:
        vocalesN += 1
    elif letra in consonantes:
        consonantesN += 1
print(f"Hola {name} {apellido}")
print(f"Tu nombre tiene {letrasN} letras y {vocalesN} vocales. y {consonantesN} consonantes.")
