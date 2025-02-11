import requests
import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv('API_KEY')

import requests

def fetch_data(animal):
    URL = f"https://api.api-ninjas.com/v1/animals?name={animal}"
    try:
        res = requests.get(URL, headers={'X-Api-Key': API_KEY}, timeout=10)
        res.raise_for_status()  # Raises an HTTPError for bad responses
        return res.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
