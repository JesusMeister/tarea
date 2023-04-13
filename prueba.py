import requests
url = "http://127.0.0.1:8000/grafica"
data = {"id":1} # el cuerpo de la peticion
response = requests.post(url, json=data) # hacer la peticion POST
x = response.json()
print(x) 