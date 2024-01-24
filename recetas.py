import os
import openai
#from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

def generar_recetas(platillo):
    modelo = "gpt-3.5-turbo"
    respuesta_recetas = openai.ChatCompletion.create(
        model=modelo,
        messages=[
            {"role": "system", "content": '''Responde como chef de cocina dondome los ingredientes 
            necesarios en bullet points, debes iniciar dicindo: Los ingredientes necesarios son: .'''},
            {"role": "user", "content": platillo}
        ]
    )

    return respuesta_recetas.choices[0].message['content']

# Ejemplo de uso
#platillo = input("En que platillo te puedo ayudar hoy?: ")
#print(generar_recetas(platillo)) 