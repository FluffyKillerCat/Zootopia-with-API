def fetch_data(animal):
    URL = f"https://api.api-ninjas.com/v1/animals?name={animal}"
    res = requests.get(URL, headers={'X-Api-Key': API_KEY})
    return res.json()