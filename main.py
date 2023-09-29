import requests

url = "https://www.deprati.com.ec/es/back-to-classics/c/c/0209A574/results?q=%3Arelevance&page=1"
user_agent = {'User-agent': 'Mozilla/5.0'}


# Send an HTTP GET request
response = requests.get(url=url, headers=user_agent)

# Check if the request was successful
if response.status_code == 200:
    # Parse the response content as JSON
    data = response.json()

    # Now you can work with the JSON data
    # Example: Print the JSON data
    print(data)
else:
    print(f"Failed to retrieve the web page. Status code: {response.status_code}")