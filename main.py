import requests
#etiqueta="pantalon-classic-stefano/p/123030196722477021"

url = f"https://www.deprati.com.ec/es/back-to-classics/c/c/0209A574/results?q=%3Arelevance&page=1"
user_agent = {'User-agent': 'Mozilla/5.0'}
print(url)
resultado = requests.get(url=url, headers=user_agent)
print(resultado)


if resultado.status_code == 200:
    data = resultado.json()

    print(data)
else:
    print(f"Failed to retrieve the web page. Status code: {resultado.status_code}")