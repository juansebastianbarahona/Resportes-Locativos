import streamlit as st
import pandas as pd
from datetime import datetime
import urllib.parse

st.set_page_config(page_title="Reportes Locativos", page_icon="📋", layout="centered")

st.title("📋 Registro de Afectaciones Locativas")
st.write("Registra cualquier daño o problema en las instalaciones para reportarlo directamente al administrador.")

# Campos del formulario
nombre = st.text_input("👤 Persona que reporta:", placeholder="Ej. Juan Pérez")
ubicacion = st.selectbox("📍 Lugar desde donde reporta:", 
                        ['Edificio Principal', 'Bodega Norte', 'Bodega Naval', 'Bodega Alquilada'])
mantenimiento = st.text_input("🔧 Tipo de mantenimiento requerido (Opcional):", 
                              placeholder="Ej. Reparar luminaria, fuga de agua, pintura...")
area = st.text_input("⚠️ Área afectada:", placeholder="Ej. Oficina 201, baño de planta, techo bodega")

# Carga de imagen
imagen = st.file_uploader("📸 Subir evidencia fotográfica:", type=["jpg", "jpeg", "png"])

if st.button("✉️ Enviar Reporte por WhatsApp", type="primary"):
    if not nombre or not area:
        st.error("❌ Por favor, ingresa tu nombre y el área afectada para poder continuar.")
    else:
        # Formatear el mensaje para WhatsApp
        fecha_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        maint_txt = mantenimiento.strip() if mantenimiento.strip() else "No especificado"
        img_status = "Adjunta (enviar en el siguiente mensaje)" if imagen is not None else "No subida"
        
        mensaje = (
            f"🚨 *NUEVO REPORTE LOCATIVO* 🚨

"
            f"👤 *Por:* {nombre}
"
            f"📍 *Lugar:* {ubicacion}
"
            f"🔧 *Mantenimiento:* {maint_txt}
"
            f"⚠️ *Área Afectada:* {area}
"
            f"📅 *Fecha:* {fecha_hora}
"
            f"🖼️ *Imagen:* {img_status}

"
            f"_Enviado desde el Portal de Reportes_"
        )
        
        # Número destino con prefijo internacional (+57 320 4504969)
        numero_telefono = "573204504969"
        mensaje_codificado = urllib.parse.quote(mensaje)
        url_whatsapp = f"https://api.whatsapp.com/send?phone={numero_telefono}&text={mensaje_codificado}"
        
        st.success("✅ Reporte generado de forma exitosa.")
        st.markdown(f'''
            <a href="{url_whatsapp}" target="_blank" style="
                background-color: #25D366;
                color: white;
                padding: 12px 20px;
                text-decoration: none;
                font-weight: bold;
                border-radius: 5px;
                display: inline-block;
                margin-top: 10px;
                text-align: center;
            ">💬 Abrir WhatsApp y Enviar Reporte</a>
        ''', unsafe_allow_html=True)