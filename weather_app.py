import requests
import json

def obtener_clima(ciudad, clave_api):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={clave_api}&units=metric&lang=es"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        datos = respuesta.json()
        temperatura = datos['main']['temp']
        descripcion = datos['weather'][0]['description']
        print(f"El clima en {ciudad} es: {descripcion} con una temperatura de {temperatura}°C")
        print(json.dumps(datos, indent=4))
    else:
        print("Error al obtener los datos del clima.")

if __name__ == "__main__":
    ciudad = input("Ingresa el nombre de la ciudad para obtener el clima: ")
    clave_api = 'your_API_key'  # Reemplazar con tu API key