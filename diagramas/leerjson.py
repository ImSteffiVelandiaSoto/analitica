import requests

# URL que devuelve el JSON
url = "https://www.ejemplo.co"

try:
    # Hacer la solicitud GET
    respuesta = requests.get(url, stream=True)
    respuesta.raise_for_status()  # Lanza un error si la solicitud falla

    # Guardar directamente en un archivo JSON
    with open("datos.json", "wb") as archivo:
        for chunk in respuesta.iter_content(chunk_size=8192):  
            archivo.write(chunk)

    print("JSON guardado correctamente en 'datos.json'.")

except requests.exceptions.RequestException as e:
    print("Error al obtener los datos:", e)