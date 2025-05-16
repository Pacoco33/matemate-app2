# app_matemate.py
import streamlit as st
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

# --- Configuración general ---
st.set_page_config(page_title="MateMate", page_icon="🧠", layout="centered")

# --- Estilo personalizado (CSS) ---
st.markdown("""
    <style>
    .title {
        font-size:40px;
        font-weight:bold;
        color:#4B8BBE;
        text-align:center;
    }
    .image-frame {
        border: 4px solid #4B8BBE;
        border-radius: 15px;
        padding: 10px;
        background-color: #f9f9f9;
    }
    </style>
""", unsafe_allow_html=True)

# --- Título principal ---
st.markdown('<div class="title">🧠 MateMate: IA que explica y dibuja</div>', unsafe_allow_html=True)
st.write("¡Escribe una pregunta o una descripción y deja que nuestra IA haga magia!")

# --- API Key y cliente ---
GEMINI_API_KEY = "AIzaSyDIMQIuMT6x7320o10J4axZh15YCN6AycQ"
client = genai.Client(api_key=GEMINI_API_KEY)

# --- Entrada del usuario ---
prompt = st.text_input("✏️ ¿Qué quieres hoy jomio/jomia?", placeholder="Ej: ¿Cómo funciona la fotosíntesis? o Mapa España")

if st.button("Generar"):
    if prompt:
        with st.spinner("🧠 Dándole a la mocha..."):
            response = client.models.generate_content(
                model="gemini-2.0-flash-exp",
                contents=[prompt],
                config=types.GenerateContentConfig(
                    response_modalities=["Text", "Image"]
                ),
            )

            for part in response.candidates[0].content.parts:
                if part.text is not None:
                    st.markdown(f"### 📘 Explicación Generada\n{part.text}")
                elif part.inline_data is not None:
                    image = Image.open(BytesIO(part.inline_data.data))
                    st.markdown('<div class="image-frame">', unsafe_allow_html=True)
                    st.image(image, caption="🎨 Imagen generada por IA", use_column_width=True)
                    st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.warning("Escribe algo en el cuadro de texto para empezar.")

