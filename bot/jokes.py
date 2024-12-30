import requests

def get_joke():
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    joke = response.json()
    return f"{joke['setup']} - {joke['punchline']}"
