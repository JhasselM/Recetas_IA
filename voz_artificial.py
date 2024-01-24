import os
import requests
from recetas import generar_recetas
from dotenv import load_dotenv

#Cargar variables de entorno del archivo .env
load_dotenv()

#Obtener la clave API del archivo .env
api_key = os.getenv("XI_API_KEY")

CHUNK_SIZE = 1024
url = "https://api.elevenlabs.io/v1/text-to-speech/Ez9PwBgxFVZ8NFko3zfC"

#Ahora usa esta clave en tus headers
headers = {
  "Accept": "audio/mpeg",
  "Content-Type": "application/json",
  "xi-api-key": api_key  # Aquí usas la variable api_key
}

#llamar a la funcion Platillo en Voz_artificial
platillo = input("¿Qué receta te gustaría escuchar?: ")
respuesta_recetas = generar_recetas(platillo)
# Resto del código para la generación de audio (usando respuesta_recetas)
data = {
    "text": respuesta_recetas,
    "model_id": "eleven_monolingual_v1",
    "voice_settings": {
        "stability": 0.5,
        "similarity_boost": 0.5
    }
}

response = requests.post(url, json=data, headers=headers)

#Verifica el código de estado de la respuesta
print("Código de estado HTTP:", response.status_code)

if response.status_code == 200:
    with open('recetas.mp3', 'wb') as f:
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                f.write(chunk)
else:
    print("Hubo un error en la solicitud: ", response.text)