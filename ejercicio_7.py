import requests

url = "https://api.chucknorris.io/jokes/random"
respuesta = requests.get(url)
datos = respuesta.json()
for i in datos:
    if i == 'value':
        print(datos[i])