'''import os
import requests
from recetas import generar_recetas
from dotenv import load_dotenv

def generar_audio(respuesta_recetas, api_key_eleven):
    # Configurar API key para Eleven Labs
    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": api_key_eleven
    }

    # Resto del código para la generación de audio (usando respuesta_recetas)
    url = "https://api.elevenlabs.io/v1/text-to-speech/Ez9PwBgxFVZ8NFko3zfC"
    data = {
        "text": respuesta_recetas,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
    }

    response = requests.post(url, json=data, headers=headers)

    # Verifica el código de estado de la respuesta
    print("Código de estado HTTP:", response.status_code)

    if response.status_code == 200:
        with open('recetas.mp3', 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
    else:
        print("Hubo un error en la solicitud: ", response.text)

def main():
    load_dotenv()

    # Cargar variables de entorno del archivo .env
    api_key_openai = os.getenv("OPENAI_API_KEY")
    api_key_eleven = os.getenv("XI_API_KEY")

    # Configurar API key para OpenAI
    openai.api_key = api_key_openai

    # Ejemplo de uso de la función generar_recetas
    platillo = input("¿En qué platillo te puedo ayudar hoy?: ")
    respuesta_recetas = generar_recetas(platillo)
    print("Receta generada:", respuesta_recetas)

    # Generar audio
    generar_audio(respuesta_recetas, api_key_eleven)

if __name__ == "__main__":
    main()'''

# main.py

import os
import requests
from dotenv import load_dotenv
from recetas import generar_recetas  # Asumiendo que recetas.py está en el mismo directorio

load_dotenv()

# Obtener la clave API del archivo .env
api_key_openai = os.getenv("OPENAI_API_KEY")
api_key_elevenlabs = os.getenv("XI_API_KEY")

# Configurar OpenAI
import openai
openai.api_key = api_key_openai

# Configurar Eleven Labs
url = "https://api.elevenlabs.io/v1/text-to-speech/Ez9PwBgxFVZ8NFko3zfC"
headers = {
  "Accept": "audio/mpeg",
  "Content-Type": "application/json",
  "xi-api-key": api_key_elevenlabs
}

def main():
    platillo = input("En qué platillo te puedo ayudar hoy?: ")

    # Generar recetas usando OpenAI
    respuesta_recetas = generar_recetas(platillo)
    print("Recetas generadas:", respuesta_recetas)

    # Generar audio usando Eleven Labs
    data = {
        "text": respuesta_recetas,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
    }

    response = requests.post(url, json=data, headers=headers)

    # Verificar el código de estado de la respuesta
    print("Código de estado HTTP:", response.status_code)

    if response.status_code == 200:
        with open('recetas.mp3', 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
    else:
        print("Hubo un error en la solicitud: ", response.text)

if __name__ == "__main__":
    main()
