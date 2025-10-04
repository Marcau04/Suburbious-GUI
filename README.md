# 🏙️ Suburbious-GUI

**Suburbious-GUI** es una versión ampliada del juego **Suburbious** desarrollada en **Python**, ahora con **interfaz gráfica** creada con **wxPython (wxGlade)**.  
El juego combina mecánicas de *puzzle* tipo *match-3* con evolución de piezas y gestión de enemigos (Bigfoots).  

---

## 🎮 Mecánicas principales

- **Evolución de letras:**  
  `a → b → c → d → e`  
  Cuando se juntan 3 o más iguales, se transforman en la ficha del nivel superior.  

- **Bigfoots:**  
  - **1 (libre):** se mueve en orden de prioridad (arriba → derecha → abajo → izquierda) y envejece cada turno.  
  - Al llegar a **edad 10**, se convierte en un **escombro (X)** que bloquea permanentemente la celda.  
  - **2 (encerrado):** aparece cuando un `1` queda rodeado.  
    - `2+2+2 → 3 (casa)`  
    - `3+3+3 → 4 (hotel)`  

- **Wicks:**  
  - Permiten eliminar el contenido de una celda ocupada.  
  - ⚠️ No se pueden usar en celdas vacías.  

---

## 🖥️ Interfaz gráfica

Opciones principales en el menú inicial:
- **Nueva partida**  
  - Cargar tablero desde fichero (`.txt`).  
  - Crear tablero aleatorio **6x6**.  
  - Crear tablero aleatorio con tamaño personalizado.  
- **Juego con límite de tiempo**  
  - Cada turno dura **10 segundos**.  
  - Si el tiempo expira, la partida termina en derrota.  

En el tablero:
- Haz clic en una celda para colocar la ficha actual.  
- Usa el botón de **almacén (`*`)** para guardar o intercambiar la ficha.  
- El juego termina si no quedan celdas libres o se agota el tiempo.  

---

## 🏆 Condiciones de victoria y derrota

- **Ganas puntos** por generar letras, casas y hoteles.  
- **Pierdes puntos** por Bigfoots, escombros y errores de jugada.  
- **Derrota:**  
  - No quedan celdas libres.  
  - Se agota el tiempo en modo contrarreloj.  

---

## 🛠️ Tecnologías utilizadas
- Lenguaje: **Python 3**  
- Librerías:  
  - `wxPython` (interfaz gráfica, diseñada con wxGlade)  
  - `random` (generación de tableros aleatorios)  

---

## 🚀 Instalación y ejecución

### 1. Clonar repositorio

### 2. Instalar dependencias
```bash
pip install wxPython
```
### 3. Ejecutar el juego
```bash
python Parte2PracticaPAR.py
```

---

## 📂 Archivos de entrada

Si se inicia desde fichero, el formato es:

- Cada celda representada por un carácter (a–e, 1–4, X, W para Wick).

- El tamaño del tablero se infiere del número de filas y columnas.



