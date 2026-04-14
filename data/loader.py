import requests

def load_data():
    url = "https://data.cityofnewyork.us/resource/jb7j-dtam.json"

    response = requests.get(url)
    data = response.json()

    # беремо тільки перші 10 записів
    return data[:10]