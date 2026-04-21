# Ejercicios de Python

<div align="center">
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" width="100" height="100" alt="Python Logo" />
  <h1>Repositorio de Práctica de Python</h1>
  <p><strong>Colección completa de ejercicios de Python para mejorar tus habilidades en lógica, fundamentos y resolución de problemas</strong></p>
  <p>
    <a href="https://www.python.org/">
      <img src="https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white" alt="Python 3.8+" />
    </a>
    <a href="https://github.com/">
      <img src="https://img.shields.io/badge/GitHub-Repository-black?logo=github" alt="GitHub Repository" />
    </a>
    <a href="#">
      <img src="https://img.shields.io/badge/Status-Active-success" alt="Status: Active" />
    </a>
    <a href="https://opensource.org/licenses/MIT">
      <img src="https://img.shields.io/badge/License-MIT-green" alt="License: MIT" />
    </a>
    <a href="https://github.com/your-username/python-Duocuc/stargazers">
      <img src="https://img.shields.io/github/stars/your-username/python-Duocuc?style=social" alt="GitHub Stars" />
    </a>
  </p>
</div>

---

## Tabla de Contenidos

- [Descripción](#descripción)
- [Características](#características)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Requisitos Previos](#requisitos-previos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Ejercicios Incluidos](#ejercicios-incluidos)
- [Progreso de Aprendizaje](#progreso-de-aprendizaje)
- [Hoja de Ruta](#hoja-de-ruta)
- [Contribuyendo](#contribuyendo)
- [Licencia](#licencia)
- [Autor](#autor)

---

## Descripción

Este repositorio es una colección exhaustiva de ejercicios prácticos de Python diseñados específicamente para estudiantes y desarrolladores que desean fortalecer sus habilidades en programación. Cada ejercicio está cuidadosamente estructurado para cubrir conceptos fundamentales y avanzados, desde lógica básica hasta estructuras de control complejas.

**¿Por qué este repositorio?**
- Aprendizaje progresivo y estructurado
- Ejemplos reales y aplicables
- Código comentado y explicaciones detalladas
- Categorización por temas y dificultad
- Comunidad activa de aprendizaje

---

## Características

- **Fundamentos Sólidos**: Cubre variables, tipos de datos, operadores y estructuras básicas
- **Control de Flujo**: Ejercicios con condicionales (if/elif/else) y bucles (for/while)
- **Desarrollo de Lógica**: Problemas que estimulan el pensamiento algorítmico
- **Resolución de Problemas**: Casos prácticos del mundo real
- **Aprendizaje Continuo**: Nuevo contenido agregado regularmente
- **Comunidad**: Comparte y aprende con otros desarrolladores

---

## Estructura del Proyecto

```
python-Duocuc/
│
├── ejerecicios en clase/
│   ├── largo-username.py          # Validación de longitud de username
│   └── verificacion-password.py    # Verificación de contraseña segura
│
├── for/
│   ├── pedir-nombre-user.py        # Solicitar nombre de usuario con bucles
│   ├── promedio-students.py        # Calcular promedio de estudiantes
│   └── promedio.py                 # Cálculo básico de promedios
│
├── if/
│   ├── notas.py                    # Sistema de calificaciones con condicionales
│   ├── test.py                     # Pruebas de lógica condicional
│   └── Tienda(If).py               # Simulación de tienda con decisiones
│
├── inicio.py                       # Archivo de inicio del proyecto
├── README.md                       # Documentación del proyecto
└── .gitignore                      # Archivos ignorados por Git
```

---

## Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:

- **Python 3.8 o superior** - [Descargar Python](https://www.python.org/downloads/)
- **Git** (opcional, para clonar el repositorio) - [Descargar Git](https://git-scm.com/downloads)
- **Editor de código** (recomendado: VS Code, PyCharm) - [Descargar VS Code](https://code.visualstudio.com/)

**Verificar instalación:**
```bash
python --version
# Debería mostrar Python 3.8.x o superior
```

---

## Instalación

### Opción 1: Clonar el repositorio
```bash
git clone https://github.com/your-username/python-Duocuc.git
cd python-Duocuc
```

### Opción 2: Descargar ZIP
1. Ve a [https://github.com/your-username/python-Duocuc](https://github.com/your-username/python-Duocuc)
2. Haz clic en "Code" > "Download ZIP"
3. Extrae el archivo y navega a la carpeta

---

## Uso

### Ejecutar un ejercicio específico
```bash
# Navega al directorio del proyecto
cd python-Duocuc

# Ejecuta cualquier archivo .py
python inicio.py
python for/promedio.py
python if/notas.py
```

### Ejemplo de ejecución
```bash
$ python for/promedio.py
Ingrese la cantidad de notas: 3
Ingrese nota 1: 85
Ingrese nota 2: 90
Ingrese nota 3: 78
El promedio es: 84.33
```

### Modo interactivo (recomendado para aprendizaje)
```python
# Abre Python en modo interactivo
python -i inicio.py

# O ejecuta directamente
python
>>> import inicio
>>> # Explora las funciones disponibles
```

---

## Ejercicios Incluidos

| Categoría | Archivo | Descripción | Nivel |
|-------------|-----------|---------------|---------|
| **Inicio** | `inicio.py` | Introducción al proyecto y funciones básicas | Principiante |
| **Ejercicios en Clase** | `largo-username.py` | Validar longitud de nombre de usuario | Principiante |
| | `verificacion-password.py` | Verificar fortaleza de contraseña | Intermedio |
| **Bucles For** | `pedir-nombre-user.py` | Solicitar input con validación | Principiante |
| | `promedio-students.py` | Calcular promedios de estudiantes | Intermedio |
| | `promedio.py` | Cálculo básico de promedios | Principiante |
| **Condicionales If** | `notas.py` | Sistema de calificaciones | Intermedio |
| | `test.py` | Pruebas de lógica condicional | Principiante |
| | `Tienda(If).py` | Simulación de compras en tienda | Intermedio |

### Detalles de Ejercicios

#### Inicio
- **Propósito**: Punto de entrada al proyecto
- **Conceptos**: Importaciones, funciones básicas
- **Tiempo estimado**: 5-10 minutos

#### Ejercicios en Clase
- **Validación de Username**: Practica manejo de strings y condicionales
- **Verificación de Password**: Implementa reglas de seguridad básicas

#### Bucles For
- **Input con Validación**: Uso de bucles para entrada de datos
- **Cálculos Estadísticos**: Promedios y operaciones matemáticas
- **Iteración sobre Datos**: Trabajo con listas y colecciones

#### Condicionales If
- **Sistema de Notas**: Conversión de números a letras
- **Lógica de Decisión**: Tomar acciones basadas en condiciones
- **Simulación Empresarial**: Aplicación práctica en escenarios reales

---

## Progreso de Aprendizaje

### Nivel Principiante
- Variables y tipos de datos
- Operadores básicos
- Entrada y salida de datos
- Comentarios y documentación

### Nivel Intermedio
- Estructuras de control (if/for/while)
- Funciones y modularidad
- Manejo de errores básico
- Trabajo con listas y diccionarios

### Nivel Avanzado (Próximamente)
- Programación orientada a objetos
- Manejo de archivos
- APIs y requests
- Bases de datos

**Consejos para aprender:**
- Lee el código antes de ejecutarlo
- Modifica los ejercicios para experimentar
- Agrega comentarios explicando cada línea
- Comparte tus soluciones en issues

---

## Hoja de Ruta



---

## Contribuyendo

¡Las contribuciones son bienvenidas! Este proyecto vive gracias a la comunidad.

### Cómo contribuir

1. **Fork el repositorio**
   ```bash
   git clone https://github.com/your-username/python-Duocuc.git
   ```

2. **Crea una rama para tu feature**
   ```bash
   git checkout -b feature/nueva-funcionalidad
   ```

3. **Desarrolla tu contribución**
   - Agrega nuevos ejercicios
   - Mejora código existente
   - Corrige errores
   - Actualiza documentación

4. **Haz commit de tus cambios**
   ```bash
   git commit -m "Agrega: descripción de la nueva funcionalidad"
   ```

5. **Push y crea Pull Request**
   ```bash
   git push origin feature/nueva-funcionalidad
   ```

### Guías de Contribución

- **Código**: Sigue PEP 8 para estilo de código Python
- **Commits**: Usa mensajes descriptivos en español o inglés
- **Ejercicios**: Incluye comentarios explicativos
- **Tests**: Agrega casos de prueba cuando sea posible
- **Documentación**: Actualiza el README si agregas nuevas funcionalidades

### Reportar Issues

Si encuentras un error o tienes una sugerencia:

1. Revisa si ya existe un issue similar
2. Crea un nuevo issue con:
   - Descripción clara del problema
   - Pasos para reproducirlo
   - Código de ejemplo (si aplica)
   - Versión de Python utilizada

---

## Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

**Resumen de la Licencia MIT:**
- Uso personal y comercial permitido
- Modificación y distribución permitida
- Inclusión en proyectos propietarios
- Sin garantía de ningún tipo
- Atribución requerida

---

## Autor

**Gabriel Pedreros**
- Estudiante de Ingeniería en Computación
- Apasionado por Python y desarrollo de software
- Siempre aprendiendo nuevas tecnologías
- Contacto: [g.pedreros.becerra@gmail.com](g.pedreros.becerra@gmail.com)

### Estadísticas del Proyecto
- **Estrellas**: ¡Ayúdanos a crecer!
- **Forks**: Comparte con amigos
- **Issues**: Reporta problemas
- **Watchers**: Mantente actualizado

---

<div align="center">
  <p><strong>¡Gracias por visitar este repositorio!</strong></p>
  <p>Si te gusta el proyecto, no olvides darle una estrella en GitHub</p>
  <a href="https://www.python.org/">
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" width="60" height="60" alt="Python" />
  </a>
</div>