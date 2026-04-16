print("ingrese tres notas:")
n1=int(input("ingresa una nota : "))
n2=int(input("ingresa otra nota : "))
n3=int(input("ingresa otra nota : "))
promedio= (n1 + n2 + n3) / 3

print("tu promedio en el ramo es: ", promedio)

if promedio>=40:
    print("aprobaste el ramo")
else:
    print("reprobaste el ramo")


