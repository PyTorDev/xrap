# XRAP - Simulador Espacial Minimalista

XRAP es un proyecto experimental para crear un simulador espacial y juego de gestión controlado desde la terminal, con un panel de telemetría en tiempo real accesible desde el navegador.

---

## 🚀 Funcionalidad esperada

### 🎮 Interacción desde la terminal
- Menú inicial al ejecutar `main.py` con opciones:
  - Iniciar el juego (lanzar el servidor y abrir navegador).
  - Instalar dependencias necesarias automáticamente.
  - Salir del juego.

### 🖥️ Telemetría en navegador
- Al iniciar el juego se abre una web local (`localhost`) con:
  - Tabla de telemetría actualizada en tiempo real (valores como oxígeno, combustible, temperatura).
  - Campo de texto para escribir comandos que se envían al backend.

### 🧠 Backend (FastAPI)
- Servidor con:
  - `GET /api/telemetria`: Devuelve los datos actuales de la simulación.
  - `POST /api/comando`: Recibe y procesa comandos desde el frontend o terminal.

### 🌐 Frontend (HTML/CSS/JS)
- Página web simple:
  - Refresca la tabla de telemetría cada pocos segundos usando JavaScript.
  - Permite enviar comandos al servidor desde un input inferior.

---

## 🧱 Tecnologías principales

- Python 3
- FastAPI
- HTML + CSS + JavaScript
- Uvicorn (para servir FastAPI)

---

## 📦 Instalación (cuando esté listo)

```bash
python3 main.py
```

Desde el menú podrás instalar todo automáticamente o iniciar la partida.

---

Este proyecto crecerá paso a paso, manteniéndose lo más simple posible.