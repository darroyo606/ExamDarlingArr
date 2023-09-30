import requests
from mongodb import client
from dotenv import load_dotenv


load_dotenv()

#URL para acceso a JSON
#etiqueta = "pantalon-classic-stefano/p/123030196722477021"
url = f"https://www.deprati.com.ec/es/back-to-classics/c/c/0209A574/results?q=%3Arelevance&page=1"
user_agent = {'User-agent': 'Mozilla/5.0'}

response = requests.get(url=url, headers=user_agent)

if response.status_code == 200:
    data = response.json()

    results = data.get("results", [])

    if len(results) > 0:

        db = client.DarExam
        collection = db.productos

        for productos in results:

            code = productos.get("code")
            name = productos.get("name")
            description = productos.get("description")
            price = productos.get("price", {}).get("formattedValue")
           # stock_status = productos.get("stock_status", {}).get("stockLevelStatus", {}).get("code")

            # Inserta los productos en la base de datos MongoDB
            doc_data = {
                "code": code,
                "name": name,
                "description": description,
                "price": price,
                #"stock_status": stock_status
            }
            collection.insert_one(doc_data)
    else:
        print("No se encontraron productos en la respuesta JSON.")
else:
    print(f"Failed to retrieve the web page. Status code: {response.status_code}")