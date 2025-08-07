# MateMate: IA que explica y dibuja

Este es un proyecto desarrollado para el módulo **"Programación de Inteligencia Artificial"** del curso de especialización **"IA y Big Data"** del **IES Las Fuentezuelas**.

## Descripción

MateMate es una pequeña aplicación interactiva que permite generar **texto e imágenes** a partir de una entrada escrita por el usuario. Utiliza el modelo `gemini-2.0-flash-exp` de Google a través de una API, y está orientada a **facilitar el trabajo docente** en el aula: creación de materiales, ilustraciones educativas, comunicados, explicaciones rápidas, etc.

La app está diseñada específicamente para su despliegue en **[streamlit.io](https://streamlit.io)**, y por eso incluye secciones de **CSS personalizado** para mejorar su apariencia visual.

## Funcionalidad

- El usuario introduce una pregunta o descripción.
- La aplicación llama al modelo de Google Gemini y devuelve:
  - Una explicación textual
  - Una imagen generada (si aplica)
- El contenido se muestra en la interfaz con estilo personalizado.

## Requisitos

El archivo `requirements.txt` incluye las dependencias necesarias:

```
streamlit
google-genai
Pillow
```

## Archivos del proyecto

- `matemate_app.py`: Código fuente principal de la aplicación
- `requirements.txt`: Dependencias necesarias para ejecutar la app
- `gitattributes.txt`: Configuración básica de Git

## Ejecución local

1. Clona el repositorio.
2. Instala los requisitos:
   ```bash
   pip install -r requirements.txt
   ```
3. Crea un archivo `.streamlit/secrets.toml` con tu API key de Gemini:
   ```toml
   GEMINI_API_KEY = "tu_clave_api_aquí"
   ```
4. Ejecuta la aplicación:
   ```bash
   streamlit run matemate_app.py
   ```
