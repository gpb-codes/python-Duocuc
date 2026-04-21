usuario = input("Crea un nombre de usuario: ")

if 4 <= len(usuario) <= 10:
    print("Nombre de usuario válido")
    print("Tu nombre es válido ya que tiene", len(usuario), "caracteres")
else:
    print("El nombre de usuario debe tener entre 4 y 10 caracteres")