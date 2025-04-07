# Interfaz Tkinter para el cálculo de raíces

**Materia:** Métodos Numéricos  
**Maestro:** Solís Cisneros Horacio Irán  
**Alumno:** Silva Chacón Carlos Roberto  
**Lugar:** Tuxtla Gutiérrez, Chiapas  
**Fecha:** 06 de abril de 2025


# Manual de Usuario: Calculadora de Métodos Numéricos

## Descripción General

Esta calculadora gráfica permite encontrar raíces de funciones utilizando tres métodos numéricos:

- Método de Bisección
- Método de Falsa Posición
- Método de Newton-Raphson

La interfaz está construida con **Tkinter**, y la función ingresada se grafica usando **Matplotlib**.

---

## Requisitos del Sistema

- Python 3.x
- Bibliotecas instaladas: `matplotlib`, `numpy`, `sympy`, `tkinter`

Instalación recomendada de dependencias:

```bash
pip install matplotlib numpy sympy
```

---

## Instrucciones de Uso

### 1. Ejecutar el Programa

Ejecuta el script en un entorno de Python compatible:

```bash
python calculadora_metodos.py
```

### 2. Ingreso de Datos

La ventana principal solicita los siguientes datos:

- **Función f(x):** La función matemática a resolver. Ejemplo: `x**3 - 4*x + 1`
- **Valor a:** Límite inferior del intervalo o valor inicial.
- **Valor b:** Límite superior del intervalo (excepto en Newton-Raphson).
- **Umbral:** Se reserva para control de error.
- **Máx Inter:** Número máximo de iteraciones.
- **Método:** Selecciona uno de los tres métodos disponibles.

### 3. Ejecutar Cálculo

Haz clic en el botón **"Generar"** para ejecutar el método seleccionado.

---

## Métodos Disponibles

### Método de Bisección

- Requiere que `f(a) * f(b) < 0`
- Calcula el punto medio entre `a` y `b` y reduce el intervalo según el signo de `f(xr)`

### Método de Falsa Posición

- Similar al de Bisección, pero calcula `xr` usando interpolación lineal.

### Método de Newton-Raphson

- Utiliza la derivada de la función `f'(x)`
- Requiere valor inicial `a`
- No se permite aplicar si `f'(x) = 0`

---

## Resultados y Gráficos

- Los resultados se muestran en una tabla con los valores por iteración.
- Se grafica la función y se marca la raíz encontrada en color rojo.

---

## Posibles Errores

- **Función no válida:** Si se ingresa una expresión incorrecta.
- **Condición no cumplida:** Si no se cumple `f(a)*f(b)<0` en métodos por intervalo.
- **Derivada cero:** En Newton-Raphson, si `f'(x) = 0`.

---
