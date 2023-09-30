import requests
#Url para ingresar a los datos JSON de DEPRATI
etiqueta = "pantalon-classic-stefano/p/123030196722477021"
url = f"https://www.deprati.com.ec/es/back-to-classics/c/c/0209A574/results?q=%3Arelevance&page=1"
user_agent = {'User-agent': 'Mozilla/5.0'}
print(url)
response = requests.get(url=url, headers=user_agent)

if response.status_code == 200:
    data = response.json()

    # Ingresa a la lista de resultados
    results = data.get("results", [])

    if len(results) > 0:
        for product in results:
            # Accede a los campos del producto
            code = product.get("code")
            name = product.get("name")
            description = product.get("description")
            price = product.get("price", {}).get("formattedValue")
            stock_status = product.get("stock", {}).get("stockLevelStatus", {}).get("code")

            # Imprime la información de cada producto
            print(f"Código del producto: {code}")
            print(f"Nombre del producto: {name}")
            #print(f"Descripción: {description}")
            print(f"Precio: {price}")
            print(f"Estado de stock: {stock_status}")
            print("-" * 50)  # para separar los productos
    else:
        print("No se encontraron productos en la respuesta JSON.")
else:
    print(f"Failed to retrieve the web page. Status code: {response.status_code}")