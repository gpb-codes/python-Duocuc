import os
import subprocess
import sys

# Diccionario con los proyectos organizados por categoría
PROYECTOS = {
    "Ejercicios en Clase": {
        "ruta": "ejerecicios en clase",
        "archivos": [
            ("1. Largo de Username", "largo-username.py"),
            ("2. PIN", "pin.py"),
            ("3. Verificación de Password", "verificacion-password.py"),
        ]
    },
    "Bucles (FOR)": {
        "ruta": "for",
        "archivos": [
            ("1. Pedir Nombre de Usuario", "pedir-nombre-user.py"),
            ("2. Promedio de Estudiantes", "promedio-students.py"),
            ("3. Promedio", "promedio.py"),
        ]
    },
    "Condicionales (IF)": {
        "ruta": "if",
        "archivos": [
            ("1. Notas", "notas.py"),
            ("2. Test", "test.py"),
            ("3. Tienda", "Tienda(If).py"),
        ]
    },
}

def limpiar_pantalla():
    """Limpia la pantalla de la consola"""
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_banner():
    """Muestra el banner de inicio"""
    print("=" * 60)
    print("REPOSITORIO DE EJERCICIOS PYTHON - DUOCUC".center(60))
    print("=" * 60)
    print()

def mostrar_menu_principal():
    """Muestra el menú principal de categorías"""
    print("CATEGORÍAS DISPONIBLES:\n")
    categorias = list(PROYECTOS.keys())
    
    for i, categoria in enumerate(categorias, 1):
        print(f"  {i}. {categoria}")
    
    print(f"  {len(categorias) + 1}. Salir")
    print()

def mostrar_menu_categoria(categoria):
    """Muestra los ejercicios de una categoría específica"""
    limpiar_pantalla()
    mostrar_banner()
    
    info = PROYECTOS[categoria]
    archivos = info["archivos"]
    
    print(f"{categoria.upper()}\n")
    
    for opcion, _ in archivos:
        print(f"  {opcion}")
    
    print(f"  {len(archivos) + 1}. Volver al menú principal")
    print()

def ejecutar_archivo(ruta_completa):
    """Ejecuta un archivo Python"""
    try:
        print(f"\nEjecutando: {os.path.basename(ruta_completa)}\n")
        print("-" * 60)
        subprocess.run([sys.executable, ruta_completa])
        print("-" * 60)
        input("\nPresiona ENTER para continuar...")
    except FileNotFoundError:
        print(f"Error: El archivo no se encontró en {ruta_completa}")
        input("\nPresiona ENTER para continuar...")
    except Exception as e:
        print(f"Error al ejecutar el archivo: {e}")
        input("\nPresiona ENTER para continuar...")

def main():
    """Función principal del menú"""
    while True:
        limpiar_pantalla()
        mostrar_banner()
        mostrar_menu_principal()
        
        try:
            opcion = input("Selecciona una opción: ").strip()
            categorias = list(PROYECTOS.keys())
            
            if opcion == str(len(categorias) + 1):
                print("\n¡Hasta luego!")
                break
            
            if opcion not in [str(i) for i in range(1, len(categorias) + 1)]:
                input("Opción inválida. Presiona ENTER para continuar...")
                continue
            
            categoria_seleccionada = categorias[int(opcion) - 1]
            
            while True:
                mostrar_menu_categoria(categoria_seleccionada)
                info = PROYECTOS[categoria_seleccionada]
                archivos = info["archivos"]
                
                try:
                    opcion_archivo = input("Selecciona un ejercicio: ").strip()
                    
                    if opcion_archivo == str(len(archivos) + 1):
                        break
                    
                    if opcion_archivo not in [str(i) for i in range(1, len(archivos) + 1)]:
                        input("Opción inválida. Presiona ENTER para continuar...")
                        continue
                    
                    nombre_archivo = archivos[int(opcion_archivo) - 1][1]
                    ruta_completa = os.path.join(
                        os.path.dirname(__file__),
                        info["ruta"],
                        nombre_archivo
                    )
                    
                    limpiar_pantalla()
                    ejecutar_archivo(ruta_completa)
                    
                except KeyboardInterrupt:
                    break
        
        except KeyboardInterrupt:
            print("\n\n¡Hasta luego!")
            break

if __name__ == "__main__":
    main()
