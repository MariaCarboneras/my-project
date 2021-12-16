import requests
url = "https://ammtp.pythonanywhere.com/testapp/post_example"
response = requests.get(url)

param1 = '1'
param2 = '2'

parametros = {
    "param1": param1,
    "param2": param2,
}

data="123"

response.request.post(url, params=parametros, data=data)

print(response.text)

valor1= response.json()[]


assert valor1 == param1
assert valor2 == param2
assert valor3 == data