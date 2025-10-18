# 🧠 Cuántica Básica: Observables y Medidas

Este repositorio contiene un **notebook interactivo en Jupyter** titulado **“Cuántica básica, observables y medidas”**, que introduce y desarrolla conceptos fundamentales de la **mecánica cuántica**, incluyendo:

- Representación matemática de estados cuánticos  
- Observables y operadores lineales  
- Proceso de medición y colapso del estado  
- Cálculos de valores esperados y probabilidades  
- Ejemplos computacionales y visualizaciones

---

## 📁 Estructura del repositorio

```
📦 Cuantica-Basica
 ┣ 📜 README.md
 ┣ 📓 Cuantica basica, observables y medidas.ipynb
 ┣ 📜 requirements.txt
 ┗ 📓 transcription_quantum_chapter.py
```

---

## ⚙️ Requisitos

Asegúrate de tener instalado **Python 3.9+** y **Jupyter Notebook**.  
Las principales librerías necesarias son:

```bash
pip install numpy scipy matplotlib pandas sympy
```

Librerías adicionales que también podrían requerirse (dependiendo del código del notebook):

```bash
pip install fractions itertools IPython
```

---

## ▶️ Cómo ejecutar el notebook

1. **Clona el repositorio** desde GitHub:
   ```bash
   git clone https://github.com/JuanTellez125/CNYT.git
   cd CNYT
   ```

2. **Abre Jupyter Notebook**:
   ```bash
   jupyter notebook
   ```

3. En el navegador, abre el archivo:
   ```
   Cuantica basica, observables y medidas.ipynb
   ```

4. **Ejecuta las celdas** en orden (`Shift + Enter`) para reproducir los cálculos, gráficas y simulaciones.

---

## 📘 Contenidos principales

El notebook está dividido en secciones teóricas y prácticas:

1. **Introducción a la Mecánica Cuántica**  
   Breve repaso de postulados y formalismo matemático.

2. **Espacios de Hilbert y vectores de estado**  
   Representación de estados mediante vectores y matrices.

3. **Observables y operadores hermitianos**  
   Cómo se modelan magnitudes físicas en el espacio de estados.

4. **Medición cuántica**  
   Ejemplo del colapso del estado y cálculo de probabilidades.

5. **Ejercicios computacionales**  
   Uso de `numpy`, `sympy` y `matplotlib` para cálculos y visualización de resultados.

---

## 📊 Ejemplo de ejecución

```python
import numpy as np
import matplotlib.pyplot as plt

# Estado cuántico simple
psi = np.array([1/np.sqrt(2), 1/np.sqrt(2)])

# Observable: matriz de Pauli Z
sigma_z = np.array([[1, 0], [0, -1]])

# Valor esperado
exp_val = np.vdot(psi, sigma_z @ psi)
print(f"Valor esperado de σz: {exp_val}")
```

Salida:
```
Valor esperado de σz: 0.0
```

---

## 🧩 Créditos

Creado por **Juan Tellez**  
Universidad: *Escuela Colombiana de Ingenieria Julio Garavito* 
curso: *CNYT (Ciencias Naturales y Tecnologia)* 
Versión: 1.0 — Octubre 2025
